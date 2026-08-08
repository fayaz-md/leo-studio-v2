import unittest

from studio.voice_engine.voice_engine import (
    VoiceEngine,
)


class TestVoiceEngine(unittest.TestCase):

    def setUp(self):

        self.engine = VoiceEngine()

    def test_processes_all_known_dialogues(self):

        dialogues = [
            {
                "speaker": "Leo",
                "text": "हमें उसकी मदद करनी होगी!",
            },
            {
                "speaker": "Meera",
                "text": "रुको लियो!",
            },
            {
                "speaker": "Robbie",
                "text": "खतरा detected!",
            },
        ]

        results = self.engine.process(
            dialogues
        )

        self.assertEqual(
            len(results),
            3,
        )

    def test_assigns_correct_voice_ids(self):

        dialogues = [
            {
                "speaker": "Leo",
                "text": "Hello",
            },
            {
                "speaker": "Meera",
                "text": "Hello",
            },
            {
                "speaker": "Robbie",
                "text": "Hello",
            },
        ]

        results = self.engine.process(
            dialogues
        )

        voice_ids = [
            result["voice_id"]
            for result in results
        ]

        self.assertEqual(
            voice_ids,
            [
                "leo_v1",
                "meera_v1",
                "robbie_v1",
            ],
        )

    def test_preserves_dialogue_text(self):

        dialogues = [
            {
                "speaker": "Leo",
                "text": "हमें उसकी मदद करनी होगी!",
            },
        ]

        results = self.engine.process(
            dialogues
        )

        self.assertEqual(
            results[0]["text"],
            "हमें उसकी मदद करनी होगी!",
        )

    def test_preserves_speaker(self):

        dialogues = [
            {
                "speaker": "Meera",
                "text": "रुको लियो!",
            },
        ]

        results = self.engine.process(
            dialogues
        )

        self.assertEqual(
            results[0]["speaker"],
            "Meera",
        )

    def test_includes_voice_profile(self):

        dialogues = [
            {
                "speaker": "Leo",
                "text": "Let's go!",
            },
        ]

        results = self.engine.process(
            dialogues
        )

        self.assertIn(
            "voice_profile",
            results[0],
        )

        self.assertEqual(
            results[0]["voice_profile"][
                "voice_id"
            ],
            "leo_v1",
        )

    def test_unknown_speaker_is_skipped(self):

        dialogues = [
            {
                "speaker": "Unknown",
                "text": "Hello",
            },
            {
                "speaker": "Leo",
                "text": "Hello",
            },
        ]

        results = self.engine.process(
            dialogues
        )

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0]["voice_id"],
            "leo_v1",
        )

    def test_empty_dialogues(self):

        results = self.engine.process(
            []
        )

        self.assertEqual(
            results,
            [],
        )

    def test_none_dialogues(self):

        results = self.engine.process(
            None
        )

        self.assertEqual(
            results,
            [],
        )


if __name__ == "__main__":
    unittest.main()