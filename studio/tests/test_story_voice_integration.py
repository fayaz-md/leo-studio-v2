import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from studio.pipelines.voice_pipeline import (
    VoicePipeline,
)


class TestStoryVoiceIntegration(unittest.TestCase):

    def test_dialogue_metadata_reaches_renderer(self):

        dialogue = SimpleNamespace(
            speaker="leo",
            text="चलो दोस्तों!",
            emotion="excited",
            voice_style="energetic",
            speaking_speed="fast",
            pause_after=0.5,
        )

        scene = SimpleNamespace(
            dialogues=[dialogue]
        )

        story = SimpleNamespace(
            scenes=[scene]
        )

        pipeline = VoicePipeline()

        pipeline.renderer = MagicMock()

        pipeline.renderer.render.return_value = {
            "speaker": "leo",
            "audio_path": "output/audio/test.wav",
        }

        results = pipeline.process(
            story,
            output_dir="output/test_voice_integration",
        )

        self.assertEqual(
            len(results),
            1,
        )

        pipeline.renderer.render.assert_called_once()

        rendered_dialogue = (
            pipeline.renderer.render.call_args.args[0]
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
            "excited",
        )

        self.assertEqual(
            rendered_dialogue["voice_style"],
            "energetic",
        )

        self.assertEqual(
            rendered_dialogue["speaking_speed"],
            "fast",
        )

        self.assertEqual(
            rendered_dialogue["pause_after"],
            0.5,
        )


if __name__ == "__main__":
    unittest.main()