import unittest
from unittest.mock import MagicMock, patch


class TestVoicePipeline(unittest.TestCase):

    @patch(
        "studio.pipelines.voice_pipeline.VoiceRenderer"
    )
    def test_processes_story_dialogues(
        self,
        mock_renderer_class,
    ):

        from studio.pipelines.voice_pipeline import (
            VoicePipeline,
        )

        mock_renderer = MagicMock()

        mock_renderer.render.side_effect = [
            {
                "speaker": "Leo",
                "voice_id": "leo_v1",
                "provider": "sarvam",
                "provider_voice_id": "shubh",
                "language_code": "hi-IN",
                "text": "चलो चलते हैं!",
                "audio_path": "output/audio/scene_01_leo_001.wav",
            },
            {
                "speaker": "Meera",
                "voice_id": "meera_v1",
                "provider": "sarvam",
                "provider_voice_id": "priya",
                "language_code": "hi-IN",
                "text": "रुको लियो!",
                "audio_path": "output/audio/scene_01_meera_002.wav",
            },
        ]

        mock_renderer_class.return_value = (
            mock_renderer
        )

        dialogue_1 = MagicMock()
        dialogue_1.speaker = "Leo"
        dialogue_1.text = "चलो चलते हैं!"

        dialogue_2 = MagicMock()
        dialogue_2.speaker = "Meera"
        dialogue_2.text = "रुको लियो!"

        scene = MagicMock()

        scene.dialogues = [
            dialogue_1,
            dialogue_2,
        ]

        story = MagicMock()

        story.scenes = [
            scene,
        ]

        pipeline = VoicePipeline()

        results = pipeline.process(
            story,
            "test_output/audio",
        )

        self.assertEqual(
            len(results),
            2,
        )

        self.assertEqual(
            results[0]["speaker"],
            "Leo",
        )

        self.assertEqual(
            results[0]["voice_id"],
            "leo_v1",
        )

        self.assertEqual(
            results[1]["speaker"],
            "Meera",
        )

        self.assertEqual(
            results[1]["voice_id"],
            "meera_v1",
        )

        self.assertEqual(
            mock_renderer.render.call_count,
            2,
        )

    @patch(
        "studio.pipelines.voice_pipeline.VoiceRenderer"
    )
    def test_skips_dialogue_without_speaker(
        self,
        mock_renderer_class,
    ):

        from studio.pipelines.voice_pipeline import (
            VoicePipeline,
        )

        mock_renderer_class.return_value = (
            MagicMock()
        )

        dialogue = MagicMock()

        dialogue.speaker = ""
        dialogue.text = "Hello!"

        scene = MagicMock()

        scene.dialogues = [
            dialogue,
        ]

        story = MagicMock()

        story.scenes = [
            scene,
        ]

        pipeline = VoicePipeline()

        results = pipeline.process(
            story,
            "test_output/audio",
        )

        self.assertEqual(
            results,
            [],
        )

        mock_renderer_class.return_value.render.assert_not_called()

    @patch(
        "studio.pipelines.voice_pipeline.VoiceRenderer"
    )
    def test_skips_dialogue_without_text(
        self,
        mock_renderer_class,
    ):

        from studio.pipelines.voice_pipeline import (
            VoicePipeline,
        )

        mock_renderer_class.return_value = (
            MagicMock()
        )

        dialogue = MagicMock()

        dialogue.speaker = "Leo"
        dialogue.text = ""

        scene = MagicMock()

        scene.dialogues = [
            dialogue,
        ]

        story = MagicMock()

        story.scenes = [
            scene,
        ]

        pipeline = VoicePipeline()

        results = pipeline.process(
            story,
            "test_output/audio",
        )

        self.assertEqual(
            results,
            [],
        )

        mock_renderer_class.return_value.render.assert_not_called()

    @patch(
        "studio.pipelines.voice_pipeline.VoiceRenderer"
    )
    def test_multiple_scenes(
        self,
        mock_renderer_class,
    ):

        from studio.pipelines.voice_pipeline import (
            VoicePipeline,
        )

        mock_renderer = MagicMock()

        mock_renderer.render.side_effect = [
            {
                "speaker": "Leo",
                "voice_id": "leo_v1",
            },
            {
                "speaker": "Robbie",
                "voice_id": "robbie_v1",
            },
        ]

        mock_renderer_class.return_value = (
            mock_renderer
        )

        dialogue_1 = MagicMock()

        dialogue_1.speaker = "Leo"
        dialogue_1.text = "चलो!"

        dialogue_2 = MagicMock()

        dialogue_2.speaker = "Robbie"
        dialogue_2.text = "खतरा!"

        scene_1 = MagicMock()

        scene_1.dialogues = [
            dialogue_1,
        ]

        scene_2 = MagicMock()

        scene_2.dialogues = [
            dialogue_2,
        ]

        story = MagicMock()

        story.scenes = [
            scene_1,
            scene_2,
        ]

        pipeline = VoicePipeline()

        results = pipeline.process(
            story,
            "test_output/audio",
        )

        self.assertEqual(
            len(results),
            2,
        )

        first_call = (
            mock_renderer.render.call_args_list[0]
        )

        second_call = (
            mock_renderer.render.call_args_list[1]
        )

        self.assertIn(
            "scene_01_leo_001.wav",
            first_call.args[1],
        )

        self.assertIn(
            "scene_02_robbie_001.wav",
            second_call.args[1],
        )

    @patch(
        "studio.pipelines.voice_pipeline.VoiceRenderer"
    )
    def test_empty_story(
        self,
        mock_renderer_class,
    ):

        from studio.pipelines.voice_pipeline import (
            VoicePipeline,
        )

        mock_renderer_class.return_value = (
            MagicMock()
        )

        story = MagicMock()

        story.scenes = []

        pipeline = VoicePipeline()

        results = pipeline.process(
            story,
            "test_output/audio",
        )

        self.assertEqual(
            results,
            [],
        )

    @patch(
        "studio.pipelines.voice_pipeline.VoiceRenderer"
    )
    def test_none_story_raises_error(
        self,
        mock_renderer_class,
    ):

        from studio.pipelines.voice_pipeline import (
            VoicePipeline,
        )

        mock_renderer_class.return_value = (
            MagicMock()
        )

        pipeline = VoicePipeline()

        with self.assertRaises(
            ValueError
        ):

            pipeline.process(
                None,
                "test_output/audio",
            )


if __name__ == "__main__":
    unittest.main()