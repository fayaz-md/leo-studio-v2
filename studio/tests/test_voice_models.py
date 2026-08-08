import unittest

from studio.voice_engine.voice_models import (
    VoiceModels,
)


class TestVoiceModels(unittest.TestCase):

    def test_leo_voice_exists(self):

        voice = VoiceModels.get("leo")

        self.assertIsNotNone(voice)
        self.assertEqual(
            voice["voice_id"],
            "leo_v1",
        )

    def test_meera_voice_exists(self):

        voice = VoiceModels.get("meera")

        self.assertIsNotNone(voice)
        self.assertEqual(
            voice["voice_id"],
            "meera_v1",
        )

    def test_robbie_voice_exists(self):

        voice = VoiceModels.get("robbie")

        self.assertIsNotNone(voice)
        self.assertEqual(
            voice["voice_id"],
            "robbie_v1",
        )

    def test_voice_ids_are_unique(self):

        voices = [
            VoiceModels.get("leo"),
            VoiceModels.get("meera"),
            VoiceModels.get("robbie"),
        ]

        voice_ids = [
            voice["voice_id"]
            for voice in voices
        ]

        self.assertEqual(
            len(voice_ids),
            len(set(voice_ids)),
        )

    def test_character_ids_are_unique(self):

        voices = [
            VoiceModels.get("leo"),
            VoiceModels.get("meera"),
            VoiceModels.get("robbie"),
        ]

        character_ids = [
            voice["character_id"]
            for voice in voices
        ]

        self.assertEqual(
            len(character_ids),
            len(set(character_ids)),
        )

    def test_unknown_character_returns_none(self):

        self.assertIsNone(
            VoiceModels.get("unknown")
        )

    def test_voice_profiles_have_required_fields(self):

        required_fields = {
            "voice_id",
            "character_id",
            "gender",
            "age_style",
            "pitch",
            "speed",
            "energy",
            "tone",
            "emotion",
            "style",
            "language",
            "description",
        }

        for character_id in (
            "leo",
            "meera",
            "robbie",
        ):

            voice = VoiceModels.get(
                character_id
            )

            self.assertTrue(
                required_fields.issubset(
                    voice.keys()
                )
            )


if __name__ == "__main__":
    unittest.main()