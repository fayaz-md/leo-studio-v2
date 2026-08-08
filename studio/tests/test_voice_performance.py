import unittest

from studio.voice_engine.voice_performance import (
    VoicePerformance,
)


class TestVoicePerformance(unittest.TestCase):

    def setUp(self):

        self.performance = (
            VoicePerformance()
        )

    def test_default_performance(self):

        result = self.performance.build()

        self.assertEqual(
            result["pace"],
            1.05,
        )

        self.assertEqual(
            result["temperature"],
            0.75,
        )

        self.assertNotIn(
            "pitch",
            result,
        )

        self.assertNotIn(
            "loudness",
            result,
        )

    def test_excited_emotion(self):

        result = self.performance.build(
            emotion="excited"
        )

        self.assertEqual(
            result["pace"],
            1.15,
        )

        self.assertEqual(
            result["temperature"],
            0.9,
        )

    def test_sad_emotion(self):

        result = self.performance.build(
            emotion="sad"
        )

        self.assertEqual(
            result["pace"],
            0.85,
        )

        self.assertEqual(
            result["temperature"],
            0.65,
        )

    def test_voice_style_overrides_emotion_values(
        self,
    ):

        result = self.performance.build(
            emotion="happy",
            voice_style="soft",
        )

        self.assertEqual(
            result["pace"],
            0.9,
        )

        self.assertEqual(
            result["temperature"],
            0.75,
        )

    def test_speaking_speed_overrides_pace(
        self,
    ):

        result = self.performance.build(
            emotion="happy",
            speaking_speed="fast",
        )

        self.assertEqual(
            result["pace"],
            1.12,
        )

    def test_very_fast_speed(self):

        result = self.performance.build(
            speaking_speed="very_fast"
        )

        self.assertEqual(
            result["pace"],
            1.25,
        )

    def test_unknown_emotion_uses_defaults(
        self,
    ):

        result = self.performance.build(
            emotion="unknown_emotion"
        )

        self.assertEqual(
            result["pace"],
            1.0,
        )

        self.assertEqual(
            result["temperature"],
            0.6,
        )

    def test_case_insensitive_values(self):

        result = self.performance.build(
            emotion="EXCITED",
            voice_style="ENERGETIC",
            speaking_speed="FAST",
        )

        self.assertEqual(
            result["pace"],
            1.12,
        )

        self.assertEqual(
            result["temperature"],
            0.85,
        )

    def test_combined_performance(self):

        result = self.performance.build(
            emotion="worried",
            voice_style="soft",
            speaking_speed="slow",
        )

        self.assertEqual(
            result["pace"],
            0.88,
        )

        self.assertEqual(
            result["temperature"],
            0.7,
        )


if __name__ == "__main__":
    unittest.main()