import unittest

from studio.voice_engine.voice_assignment import (
    VoiceAssignment,
)


class TestVoiceAssignment(unittest.TestCase):

    def setUp(self):

        self.assignment = VoiceAssignment()

    def test_leo_assignment(self):

        dialogue = {
            "speaker": "Leo",
            "text": "हमें उसकी मदद करनी होगी!",
        }

        result = self.assignment.assign(
            dialogue
        )

        self.assertIsNotNone(result)

        self.assertEqual(
            result["speaker"],
            "Leo",
        )

        self.assertEqual(
            result["voice_id"],
            "leo_v1",
        )

        self.assertEqual(
            result["character_id"],
            "leo",
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

    def test_meera_assignment(self):

        dialogue = {
            "speaker": "Meera",
            "text": "रुको लियो!",
        }

        result = self.assignment.assign(
            dialogue
        )

        self.assertIsNotNone(result)

        self.assertEqual(
            result["voice_id"],
            "meera_v1",
        )

        self.assertEqual(
            result["character_id"],
            "meera",
        )

        self.assertEqual(
            result["provider"],
            "sarvam",
        )

        self.assertEqual(
            result["provider_voice_id"],
            "priya",
        )

        self.assertEqual(
            result["language_code"],
            "hi-IN",
        )

    def test_robbie_assignment(self):

        dialogue = {
            "speaker": "Robbie",
            "text": "खतरा detected!",
        }

        result = self.assignment.assign(
            dialogue
        )

        self.assertIsNotNone(result)

        self.assertEqual(
            result["voice_id"],
            "robbie_v1",
        )

        self.assertEqual(
            result["character_id"],
            "robbie",
        )

        self.assertEqual(
            result["provider"],
            "sarvam",
        )

        self.assertEqual(
            result["provider_voice_id"],
            "manan",
        )

        self.assertEqual(
            result["language_code"],
            "hi-IN",
        )

    def test_voice_ids_are_unique(self):

        dialogues = [
            {"speaker": "Leo", "text": "Hello"},
            {"speaker": "Meera", "text": "Hello"},
            {"speaker": "Robbie", "text": "Hello"},
        ]

        results = [
            self.assignment.assign(
                dialogue
            )
            for dialogue in dialogues
        ]

        voice_ids = [
            result["voice_id"]
            for result in results
        ]

        self.assertEqual(
            len(voice_ids),
            len(set(voice_ids)),
        )

    def test_provider_voice_ids_are_unique(self):

        dialogues = [
            {"speaker": "Leo", "text": "Hello"},
            {"speaker": "Meera", "text": "Hello"},
            {"speaker": "Robbie", "text": "Hello"},
        ]

        results = [
            self.assignment.assign(
                dialogue
            )
            for dialogue in dialogues
        ]

        provider_voice_ids = [
            result["provider_voice_id"]
            for result in results
        ]

        self.assertEqual(
            len(provider_voice_ids),
            len(set(provider_voice_ids)),
        )

    def test_unknown_speaker_returns_none(self):

        dialogue = {
            "speaker": "Unknown",
            "text": "Hello",
        }

        result = self.assignment.assign(
            dialogue
        )

        self.assertIsNone(result)

    def test_missing_speaker_returns_none(self):

        dialogue = {
            "text": "Hello",
        }

        result = self.assignment.assign(
            dialogue
        )

        self.assertIsNone(result)

    def test_empty_dialogue_returns_none(self):

        result = self.assignment.assign(
            None
        )

        self.assertIsNone(result)

    def test_voice_profile_is_attached(self):

        dialogue = {
            "speaker": "Leo",
            "text": "Let's go!",
        }

        result = self.assignment.assign(
            dialogue
        )

        self.assertIn(
            "voice_profile",
            result,
        )

        self.assertEqual(
            result["voice_profile"]["voice_id"],
            "leo_v1",
        )

        self.assertEqual(
            result["voice_profile"][
                "provider_voice_id"
            ],
            "shubh",
        )


if __name__ == "__main__":
    unittest.main()