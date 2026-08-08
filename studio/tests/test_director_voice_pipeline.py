import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from studio.director.director_pipeline import (
    DirectorPipeline,
)
from studio.pipelines.voice_pipeline import (
    VoicePipeline,
)


class TestDirectorVoicePipeline(unittest.TestCase):

    def test_director_output_flows_into_voice_pipeline(
        self,
    ):

        dialogue = SimpleNamespace(
            speaker="leo",
            text="चलो दोस्तों!",
            emotion="happy",
            voice_style="",
            speaking_speed="",
            pause_after=0.0,
            action="",
            gesture="",
        )

        scene = SimpleNamespace(
            number=1,
            dialogues=[dialogue],
            emotion="learning",
            music=None,
            camera=None,
        )

        story = SimpleNamespace(
            scenes=[scene]
        )

        # -----------------------------------------
        # Run existing DirectorPipeline
        # -----------------------------------------

        director_pipeline = (
            DirectorPipeline()
        )

        story = director_pipeline.process(
            story
        )

        # -----------------------------------------
        # VoiceDirector should enrich dialogue
        # -----------------------------------------

        self.assertEqual(
            dialogue.voice_style,
            "cheerful",
        )

        self.assertEqual(
            dialogue.speaking_speed,
            "normal",
        )

        self.assertEqual(
            dialogue.pause_after,
            0.4,
        )

        # -----------------------------------------
        # VoicePipeline with mocked renderer
        # -----------------------------------------

        voice_pipeline = VoicePipeline()

        voice_pipeline.renderer = (
            MagicMock()
        )

        voice_pipeline.renderer.render.return_value = {
            "speaker": "leo",
            "audio_path": (
                "output/audio/test.wav"
            ),
        }

        results = voice_pipeline.process(
            story,
            output_dir=(
                "output/test_director_voice"
            ),
        )

        # -----------------------------------------
        # Verify pipeline result
        # -----------------------------------------

        self.assertEqual(
            len(results),
            1,
        )

        voice_pipeline.renderer.render.assert_called_once()

        rendered_dialogue = (
            voice_pipeline
            .renderer
            .render
            .call_args.args[0]
        )

        self.assertEqual(
            rendered_dialogue["speaker"],
            "leo",
        )

        self.assertEqual(
            rendered_dialogue["text"],
            "चलो दोस्तों!",
        )

        self.assertEqual(
            rendered_dialogue["emotion"],
            "happy",
        )

        self.assertEqual(
            rendered_dialogue["voice_style"],
            "cheerful",
        )

        self.assertEqual(
            rendered_dialogue["speaking_speed"],
            "normal",
        )

        self.assertEqual(
            rendered_dialogue["pause_after"],
            0.4,
        )


if __name__ == "__main__":
    unittest.main()