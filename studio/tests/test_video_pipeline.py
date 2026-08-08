import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

from studio.pipelines.video_pipeline import (
    VideoPipeline,
)


class TestVideoPipeline(unittest.TestCase):

    def _create_scene(
        self,
        scene_number,
        duration,
    ):

        return SimpleNamespace(
            scene_number=scene_number,
            title=f"Scene {scene_number}",
            duration=duration,
            camera="static",
            image_prompt=(
                f"Image prompt {scene_number}"
            ),
            dialogues=[],
        )

    def test_render_all_scenes_and_merge(self):

        timeline = SimpleNamespace(
            total_duration=11.0,
            scenes=[
                self._create_scene(
                    scene_number=1,
                    duration=5.0,
                ),
                self._create_scene(
                    scene_number=2,
                    duration=6.0,
                ),
            ],
        )

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

            video_dir = (
                temp_dir
                / "video"
            )

            image_dir.mkdir()
            audio_dir.mkdir()

            for scene_number in [1, 2]:

                (
                    image_dir
                    / f"scene_{scene_number:02d}.png"
                ).write_bytes(
                    b"image"
                )

                (
                    audio_dir
                    / f"scene_{scene_number:02d}.wav"
                ).write_bytes(
                    b"audio"
                )

            pipeline = VideoPipeline()

            pipeline.video_provider = (
                MagicMock()
            )

            pipeline.video_provider.render_scene.side_effect = (
                lambda **kwargs: Path(
                    kwargs["output"]
                )
            )

            pipeline.video_provider.merge_scenes.side_effect = (
                lambda **kwargs: Path(
                    kwargs["output"]
                )
            )

            output_file = (
                temp_dir
                / "final.mp4"
            )

            result = pipeline.render(
                timeline=timeline,
                image_dir=image_dir,
                audio_dir=audio_dir,
                output_file=output_file,
            )

            self.assertEqual(
                result,
                output_file,
            )

            self.assertEqual(
                pipeline
                .video_provider
                .render_scene
                .call_count,
                2,
            )

            pipeline.video_provider.merge_scenes.assert_called_once()

            render_calls = (
                pipeline
                .video_provider
                .render_scene
                .call_args_list
            )

            first_call = (
                render_calls[0]
                .kwargs
            )

            second_call = (
                render_calls[1]
                .kwargs
            )

            self.assertEqual(
                Path(
                    first_call["image"]
                ).name,
                "scene_01.png",
            )

            self.assertEqual(
                Path(
                    first_call["audio"]
                ).name,
                "scene_01.wav",
            )

            self.assertEqual(
                first_call["duration"],
                5.0,
            )

            self.assertEqual(
                Path(
                    second_call["image"]
                ).name,
                "scene_02.png",
            )

            self.assertEqual(
                Path(
                    second_call["audio"]
                ).name,
                "scene_02.wav",
            )

            self.assertEqual(
                second_call["duration"],
                6.0,
            )

            merge_call = (
                pipeline
                .video_provider
                .merge_scenes
                .call_args.kwargs
            )

            self.assertEqual(
                len(
                    merge_call["scene_files"]
                ),
                2,
            )

            self.assertEqual(
                merge_call["output"],
                output_file,
            )

    def test_missing_scene_image_raises_error(self):

        timeline = SimpleNamespace(
            total_duration=5.0,
            scenes=[
                self._create_scene(
                    scene_number=1,
                    duration=5.0,
                ),
            ],
        )

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
                audio_dir
                / "scene_01.wav"
            ).write_bytes(
                b"audio"
            )

            pipeline = VideoPipeline()

            with self.assertRaises(
                FileNotFoundError
            ):

                pipeline.render(
                    timeline=timeline,
                    image_dir=image_dir,
                    audio_dir=audio_dir,
                    output_file=output_file,
                )

    def test_missing_scene_audio_raises_error(self):

        timeline = SimpleNamespace(
            total_duration=5.0,
            scenes=[
                self._create_scene(
                    scene_number=1,
                    duration=5.0,
                ),
            ],
        )

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

            pipeline = VideoPipeline()

            with self.assertRaises(
                FileNotFoundError
            ):

                pipeline.render(
                    timeline=timeline,
                    image_dir=image_dir,
                    audio_dir=audio_dir,
                    output_file=output_file,
                )


if __name__ == "__main__":
    unittest.main()