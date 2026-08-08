import base64
import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from studio.voice_engine.sarvam_provider import (
    SarvamProvider,
)


class TestSarvamProvider(unittest.TestCase):

    @patch.dict(
        os.environ,
        {
            "SARVAM_API_KEY": "test-key",
        },
        clear=False,
    )
    @patch(
        "studio.voice_engine.sarvam_provider.SarvamAI"
    )
    def test_synthesize_writes_audio(
        self,
        mock_sarvam,
    ):

        mock_client = MagicMock()

        mock_response = MagicMock()

        mock_response.audios = [
            base64.b64encode(
                b"FAKE_WAV_AUDIO"
            ).decode("ascii")
        ]

        mock_client.text_to_speech.convert.return_value = (
            mock_response
        )

        mock_sarvam.return_value = mock_client

        provider = SarvamProvider()

        voice_profile = {
            "provider": "sarvam",
            "provider_voice_id": "shubh",
            "language_code": "hi-IN",
        }

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ) as temp_file:

            output_path = temp_file.name

        try:

            result = provider.synthesize(
                text="हमें उसकी मदद करनी होगी!",
                voice_profile=voice_profile,
                output_path=output_path,
            )

            self.assertEqual(
                result,
                output_path,
            )

            with open(
                output_path,
                "rb",
            ) as file:

                content = file.read()

            self.assertEqual(
                content,
                b"FAKE_WAV_AUDIO",
            )

            mock_client.text_to_speech.convert.assert_called_once_with(
                text="हमें उसकी मदद करनी होगी!",
                language_code="hi-IN",
                speaker="shubh",
                model="bulbul:v3",
                output_audio_codec="wav",
            )

        finally:

            if os.path.exists(output_path):

                os.remove(output_path)

    @patch.dict(
        os.environ,
        {
            "SARVAM_API_KEY": "test-key",
        },
        clear=False,
    )
    @patch(
        "studio.voice_engine.sarvam_provider.SarvamAI"
    )
    def test_uses_api_key_from_environment(
        self,
        mock_sarvam,
    ):

        SarvamProvider()

        mock_sarvam.assert_called_once_with(
            api_subscription_key="test-key"
        )

    @patch.dict(
        os.environ,
        {},
        clear=True,
    )
    def test_missing_api_key_raises_error(self):

        with self.assertRaises(
            RuntimeError
        ):

            SarvamProvider()

    @patch.dict(
        os.environ,
        {
            "SARVAM_API_KEY": "test-key",
        },
        clear=False,
    )
    @patch(
        "studio.voice_engine.sarvam_provider.SarvamAI"
    )
    def test_empty_text_raises_error(
        self,
        mock_sarvam,
    ):

        provider = SarvamProvider()

        with self.assertRaises(
            ValueError
        ):

            provider.synthesize(
                text="",
                voice_profile={
                    "provider": "sarvam",
                    "provider_voice_id": "shubh",
                    "language_code": "hi-IN",
                },
                output_path="test.wav",
            )

    @patch.dict(
        os.environ,
        {
            "SARVAM_API_KEY": "test-key",
        },
        clear=False,
    )
    @patch(
        "studio.voice_engine.sarvam_provider.SarvamAI"
    )
    def test_missing_voice_profile_raises_error(
        self,
        mock_sarvam,
    ):

        provider = SarvamProvider()

        with self.assertRaises(
            ValueError
        ):

            provider.synthesize(
                text="Hello",
                voice_profile=None,
                output_path="test.wav",
            )

    @patch.dict(
        os.environ,
        {
            "SARVAM_API_KEY": "test-key",
        },
        clear=False,
    )
    @patch(
        "studio.voice_engine.sarvam_provider.SarvamAI"
    )
    def test_missing_provider_voice_raises_error(
        self,
        mock_sarvam,
    ):

        provider = SarvamProvider()

        with self.assertRaises(
            ValueError
        ):

            provider.synthesize(
                text="Hello",
                voice_profile={
                    "provider": "sarvam",
                    "language_code": "hi-IN",
                },
                output_path="test.wav",
            )


if __name__ == "__main__":
    unittest.main()