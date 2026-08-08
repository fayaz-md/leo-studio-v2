"""
Leo Studio

Voice Profile Builder

Resolves the correct voice profile for
each character before audio generation.
"""

from studio.voice_engine.voice_models import (
    VoiceModels,
)


class VoiceProfileBuilder:

    def build(self, character):

        if not character:
            return None

        character_id = character.get(
            "id",
            "",
        )

        if not character_id:
            return None

        voice = VoiceModels.get(
            character_id
        )

        if not voice:
            return None

        return {
            "voice_id": voice["voice_id"],
            "character_id": voice["character_id"],

            "provider": voice["provider"],

            "provider_voice_id": voice[
                "provider_voice_id"
            ],

            "language_code": voice[
                "language_code"
            ],

            "gender": voice["gender"],
            "age_style": voice["age_style"],
            "pitch": voice["pitch"],
            "speed": voice["speed"],
            "energy": voice["energy"],
            "tone": voice["tone"],
            "emotion": voice["emotion"],
            "style": voice["style"],
            "language": voice["language"],
            "description": voice["description"],
        }