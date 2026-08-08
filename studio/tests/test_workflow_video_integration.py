import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from studio.workflow.workflow_pipeline import (
    WorkflowPipeline,
)


class TestWorkflowVideoIntegration(unittest.TestCase):

    def _create_story(self):

        scene = SimpleNamespace(
            number=1,
            title="Leo's Adventure",
            duration=5.0,
            dialogues=[
                SimpleNamespace(
                    speaker="leo",
                    text="Hello friends!",
                    pause_after=0.4,
                )
            ],
            emotion="happy",
            camera="static",
            animation_prompt="Leo waves",
            music="cheerful",
            sfx="none",
            narration="",
            final_image_prompt=(
                "Leo standing in a sunny park"
            ),
        )

        return SimpleNamespace(
            scenes=[scene]
        )

    def test_process_with_video_inputs(self):

        story = self._create_story()

        with tempfile.TemporaryDirectory() as temp_dir:

            temp_dir = Path(temp_dir)

            image_dir = (
                temp_dir
                / "images"
            )

            audio_dir = (
                temp_dir
                / "audio"
            )

            output_file = (
                temp_dir
                / "final.mp4"
            )

            image_dir.mkdir()
            audio_dir.mkdir()

            (
                image_dir
                / "scene_01.png"
            ).write_bytes(
                b"image"
            )

            voice_file = (
                temp_dir
                / "leo.wav"
            )

            voice_file.write_bytes(
                b"voice"
            )

            with patch(
                "studio.workflow.workflow_pipeline.SceneAudioAssembler"
            ) as mock_assembler_class:

                with patch(
                    "studio.workflow.workflow_pipeline.VideoPipeline"
                ) as mock_video_class:

                    assembler = (
                        mock_assembler_class.return_value
                    )

                    video_pipeline = (
                        mock_video_class.return_value
                    )

                    assembled_audio = (
                        audio_dir
                        / "scene_01.wav"
                    )

                    def assemble_side_effect(
                        dialogues,
                        audio_files,
                        output_file,
                    ):

                        output_file = Path(
                            output_file
                        )

                        output_file.parent.mkdir(
                            parents=True,
                            exist_ok=True,
                        )

                        output_file.write_bytes(
                            b"assembled audio"
                        )

                        return output_file

                    assembler.assemble.side_effect = (
                        assemble_side_effect
                    )

                    video_pipeline.render.return_value = (
                        output_file
                    )

                    pipeline = (
                        WorkflowPipeline()
                    )

                    pipeline.voice_pipeline = (
                        MagicMock()
                    )

                    pipeline.voice_pipeline.process.return_value = [
                        {
                            "scene": 1,
                            "speaker": "leo",
                            "audio_file": voice_file,
                        }
                    ]

                    result = pipeline.process(
                        story=story,
                        image_dir=image_dir,
                        audio_dir=audio_dir,
                        output_file=output_file,
                    )

            self.assertEqual(
                result["story"],
                story,
            )

            self.assertIn(
                "voice_results",
                result,
            )

            self.assertIn(
                "timeline",
                result,
            )

            self.assertIn(
                "video_file",
                result,
            )

            self.assertEqual(
                result["video_file"],
                output_file,
            )

            pipeline.voice_pipeline.process.assert_called_once_with(
                story
            )

            assembler.assemble.assert_called_once()

            assemble_call = (
                assembler
                .assemble
                .call_args.kwargs
            )

            self.assertEqual(
                assemble_call["output_file"],
                assembled_audio,
            )

            video_pipeline.render.assert_called_once()

            render_call = (
                video_pipeline
                .render
                .call_args.kwargs
            )

            self.assertEqual(
                render_call["image_dir"],
                image_dir,
            )

            self.assertEqual(
                render_call["audio_dir"],
                audio_dir,
            )

            self.assertEqual(
                render_call["output_file"],
                output_file,
            )

    def test_process_without_story_raises_error(self):

        pipeline = WorkflowPipeline()

        with self.assertRaises(
            ValueError
        ):

            pipeline.process(
                story=None,
                image_dir="output/images",
                audio_dir="output/audio",
                output_file="output/final.mp4",
            )


if __name__ == "__main__":
    unittest.main()