import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from studio.voice_engine.voice_renderer import (
    VoiceRenderer,
)


class TestVoiceRenderer(unittest.TestCase):

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_render_leo_dialogue(
        self,
        mock_provider_class,
    ):

        mock_provider = MagicMock()

        mock_provider_class.return_value = (
            mock_provider
        )

        renderer = VoiceRenderer()

        with tempfile.TemporaryDirectory() as temp_dir:

            output_path = os.path.join(
                temp_dir,
                "leo_001.wav",
            )

            dialogue = {
                "speaker": "Leo",
                "text": "हमें उसकी मदद करनी होगी!",
            }

            result = renderer.render(
                dialogue,
                output_path,
            )

            self.assertEqual(
                result["speaker"],
                "Leo",
            )

            self.assertEqual(
                result["voice_id"],
                "leo_v1",
            )

            self.assertEqual(
                result["provider"],
                "sarvam",
            )

            self.assertEqual(
                result["provider_voice_id"],
                "shubh",
            )

            self.assertEqual(
                result["language_code"],
                "hi-IN",
            )

            self.assertEqual(
                result["text"],
                dialogue["text"],
            )

            self.assertEqual(
                result["audio_path"],
                output_path,
            )

            mock_provider.synthesize.assert_called_once()

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_render_meera_dialogue(
        self,
        mock_provider_class,
    ):

        mock_provider = MagicMock()

        mock_provider_class.return_value = (
            mock_provider
        )

        renderer = VoiceRenderer()

        with tempfile.TemporaryDirectory() as temp_dir:

            output_path = os.path.join(
                temp_dir,
                "meera_001.wav",
            )

            dialogue = {
                "speaker": "Meera",
                "text": "रुको लियो!",
            }

            result = renderer.render(
                dialogue,
                output_path,
            )

            self.assertEqual(
                result["speaker"],
                "Meera",
            )

            self.assertEqual(
                result["voice_id"],
                "meera_v1",
            )

            self.assertEqual(
                result["provider_voice_id"],
                "priya",
            )

            mock_provider.synthesize.assert_called_once()

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_render_robbie_dialogue(
        self,
        mock_provider_class,
    ):

        mock_provider = MagicMock()

        mock_provider_class.return_value = (
            mock_provider
        )

        renderer = VoiceRenderer()

        with tempfile.TemporaryDirectory() as temp_dir:

            output_path = os.path.join(
                temp_dir,
                "robbie_001.wav",
            )

            dialogue = {
                "speaker": "Robbie",
                "text": "खतरा पता चला!",
            }

            result = renderer.render(
                dialogue,
                output_path,
            )

            self.assertEqual(
                result["speaker"],
                "Robbie",
            )

            self.assertEqual(
                result["voice_id"],
                "robbie_v1",
            )

            self.assertEqual(
                result["provider_voice_id"],
                "manan",
            )

            mock_provider.synthesize.assert_called_once()

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_provider_receives_correct_text_and_profile(
        self,
        mock_provider_class,
    ):

        mock_provider = MagicMock()

        mock_provider_class.return_value = (
            mock_provider
        )

        renderer = VoiceRenderer()

        with tempfile.TemporaryDirectory() as temp_dir:

            output_path = os.path.join(
                temp_dir,
                "leo_001.wav",
            )

            dialogue = {
                "speaker": "Leo",
                "text": "चलो चलते हैं!",
            }

            renderer.render(
                dialogue,
                output_path,
            )

            call = (
                mock_provider
                .synthesize
                .call_args
            )

            self.assertEqual(
                call.kwargs["text"],
                "चलो चलते हैं!",
            )

            self.assertEqual(
                call.kwargs["output_path"],
                output_path,
            )

            self.assertEqual(
                call.kwargs[
                    "voice_profile"
                ]["provider_voice_id"],
                "shubh",
            )

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_output_directory_is_created(
        self,
        mock_provider_class,
    ):

        mock_provider = MagicMock()

        mock_provider_class.return_value = (
            mock_provider
        )

        renderer = VoiceRenderer()

        with tempfile.TemporaryDirectory() as temp_dir:

            output_path = os.path.join(
                temp_dir,
                "nested",
                "audio",
                "leo.wav",
            )

            dialogue = {
                "speaker": "Leo",
                "text": "Hello!",
            }

            renderer.render(
                dialogue,
                output_path,
            )

            self.assertTrue(
                os.path.isdir(
                    os.path.dirname(
                        output_path
                    )
                )
            )

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_unknown_speaker_raises_error(
        self,
        mock_provider_class,
    ):

        mock_provider_class.return_value = (
            MagicMock()
        )

        renderer = VoiceRenderer()

        dialogue = {
            "speaker": "Unknown",
            "text": "Hello!",
        }

        with tempfile.TemporaryDirectory() as temp_dir:

            output_path = os.path.join(
                temp_dir,
                "unknown.wav",
            )

            with self.assertRaises(
                ValueError
            ):

                renderer.render(
                    dialogue,
                    output_path,
                )

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_missing_dialogue_raises_error(
        self,
        mock_provider_class,
    ):

        mock_provider_class.return_value = (
            MagicMock()
        )

        renderer = VoiceRenderer()

        with self.assertRaises(
            ValueError
        ):

            renderer.render(
                None,
                "output.wav",
            )

    @patch(
        "studio.voice_engine.voice_renderer.SarvamProvider"
    )
    def test_missing_output_path_raises_error(
        self,
        mock_provider_class,
    ):

        mock_provider_class.return_value = (
            MagicMock()
        )

        renderer = VoiceRenderer()

        dialogue = {
            "speaker": "Leo",
            "text": "Hello!",
        }

        with self.assertRaises(
            ValueError
        ):

            renderer.render(
                dialogue,
                None,
            )


if __name__ == "__main__":
    unittest.main()