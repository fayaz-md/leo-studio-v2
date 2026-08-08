"""
Leo Studio

Sarvam Voice Provider

Converts character dialogue into audio using
Sarvam AI Bulbul TTS.
"""

import base64
import os

from sarvamai import SarvamAI


class SarvamProvider:

    def __init__(self):

        api_key = os.getenv(
            "SARVAM_API_KEY"
        )

        if not api_key:

            raise RuntimeError(
                "SARVAM_API_KEY environment "
                "variable is not set."
            )

        self.client = SarvamAI(
            api_subscription_key=api_key
        )

    def synthesize(
        self,
        text,
        voice_profile,
        output_path,
    ):

        if not text:

            raise ValueError(
                "Text cannot be empty."
            )

        if not voice_profile:

            raise ValueError(
                "Voice profile is required."
            )

        voice_id = voice_profile.get(
            "provider_voice_id"
        )

        if not voice_id:

            raise ValueError(
                "provider_voice_id is missing "
                "from voice profile."
            )

        language_code = voice_profile.get(
            "language_code",
            "hi-IN",
        )

        response = (
            self.client.text_to_speech.convert(
                text=text,
                language_code=language_code,
                speaker=voice_id,
                model="bulbul:v3",
                output_audio_codec="wav",
            )
        )

        if not response.audios:

            raise RuntimeError(
                "Sarvam returned no audio."
            )

        combined_audio = "".join(
            response.audios
        )

        audio_bytes = base64.b64decode(
            combined_audio
        )

        with open(
            output_path,
            "wb",
        ) as file:

            file.write(audio_bytes)

        return output_path