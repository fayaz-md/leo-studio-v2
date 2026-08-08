"""
Leo Studio

Voice Assignment

Assigns the correct voice profile to
each dialogue speaker.
"""

from studio.voice_engine.voice_profile_builder import (
    VoiceProfileBuilder,
)


class VoiceAssignment:

    def __init__(self):

        self.profile_builder = (
            VoiceProfileBuilder()
        )

    def assign(self, dialogue):

        if not dialogue:
            return None

        speaker = dialogue.get(
            "speaker",
            "",
        )

        if not speaker:
            return None

        character = {
            "id": speaker.lower(),
        }

        profile = self.profile_builder.build(
            character
        )

        if not profile:
            return None

        return {
            "speaker": speaker,

            "voice_id": profile[
                "voice_id"
            ],

            "character_id": profile[
                "character_id"
            ],

            "provider": profile[
                "provider"
            ],

            "provider_voice_id": profile[
                "provider_voice_id"
            ],

            "language_code": profile[
                "language_code"
            ],

            "language": profile[
                "language"
            ],

            "voice_profile": profile,
        }