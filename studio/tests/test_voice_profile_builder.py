import unittest

from studio.voice_engine.voice_profile_builder import (
    VoiceProfileBuilder,
)


class TestVoiceProfileBuilder(unittest.TestCase):

    def setUp(self):

        self.builder = VoiceProfileBuilder()

    def test_leo_profile(self):

        character = {
            "id": "leo",
            "display_name": "Leo",
        }

        profile = self.builder.build(
            character
        )

        self.assertIsNotNone(profile)

        self.assertEqual(
            profile["voice_id"],
            "leo_v1",
        )

        self.assertEqual(
            profile["character_id"],
            "leo",
        )

        self.assertEqual(
            profile["provider"],
            "sarvam",
        )

        self.assertEqual(
            profile["provider_voice_id"],
            "shubh",
        )

        self.assertEqual(
            profile["language_code"],
            "hi-IN",
        )

    def test_meera_profile(self):

        character = {
            "id": "meera",
            "display_name": "Meera",
        }

        profile = self.builder.build(
            character
        )

        self.assertIsNotNone(profile)

        self.assertEqual(
            profile["voice_id"],
            "meera_v1",
        )

        self.assertEqual(
            profile["character_id"],
            "meera",
        )

        self.assertEqual(
            profile["provider"],
            "sarvam",
        )

        self.assertEqual(
            profile["provider_voice_id"],
            "priya",
        )

        self.assertEqual(
            profile["language_code"],
            "hi-IN",
        )

    def test_robbie_profile(self):

        character = {
            "id": "robbie",
            "display_name": "Robbie",
        }

        profile = self.builder.build(
            character
        )

        self.assertIsNotNone(profile)

        self.assertEqual(
            profile["voice_id"],
            "robbie_v1",
        )

        self.assertEqual(
            profile["character_id"],
            "robbie",
        )

        self.assertEqual(
            profile["provider"],
            "sarvam",
        )

        self.assertEqual(
            profile["provider_voice_id"],
            "manan",
        )

        self.assertEqual(
            profile["language_code"],
            "hi-IN",
        )

    def test_profiles_are_unique(self):

        leo = self.builder.build(
            {"id": "leo"}
        )

        meera = self.builder.build(
            {"id": "meera"}
        )

        robbie = self.builder.build(
            {"id": "robbie"}
        )

        voice_ids = {
            leo["voice_id"],
            meera["voice_id"],
            robbie["voice_id"],
        }

        self.assertEqual(
            len(voice_ids),
            3,
        )

    def test_provider_voice_ids_are_unique(self):

        leo = self.builder.build(
            {"id": "leo"}
        )

        meera = self.builder.build(
            {"id": "meera"}
        )

        robbie = self.builder.build(
            {"id": "robbie"}
        )

        provider_voice_ids = {
            leo["provider_voice_id"],
            meera["provider_voice_id"],
            robbie["provider_voice_id"],
        }

        self.assertEqual(
            len(provider_voice_ids),
            3,
        )

    def test_unknown_character_returns_none(self):

        profile = self.builder.build(
            {"id": "unknown"}
        )

        self.assertIsNone(profile)

    def test_missing_character_returns_none(self):

        profile = self.builder.build(
            None
        )

        self.assertIsNone(profile)

    def test_missing_character_id_returns_none(self):

        profile = self.builder.build(
            {
                "display_name": "Unknown"
            }
        )

        self.assertIsNone(profile)

    def test_profile_contains_voice_properties(self):

        profile = self.builder.build(
            {"id": "leo"}
        )

        required_fields = {
            "voice_id",
            "character_id",
            "provider",
            "provider_voice_id",
            "language_code",
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

        self.assertTrue(
            required_fields.issubset(
                profile.keys()
            )
        )


if __name__ == "__main__":
    unittest.main()