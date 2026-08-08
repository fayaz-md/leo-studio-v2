"""
Leo Studio

Voice Performance

Converts dialogue emotion and speaking style
into provider-independent voice performance
parameters.
"""


class VoicePerformance:

    DEFAULTS = {
        "pace": 1.0,
        "temperature": 0.6,
    }

    EMOTION_MAP = {
        "happy": {
            "pace": 1.05,
            "temperature": 0.75,
        },
        "excited": {
            "pace": 1.15,
            "temperature": 0.9,
        },
        "sad": {
            "pace": 0.85,
            "temperature": 0.65,
        },
        "worried": {
            "pace": 0.9,
            "temperature": 0.7,
        },
        "angry": {
            "pace": 1.1,
            "temperature": 0.85,
        },
        "scared": {
            "pace": 1.1,
            "temperature": 0.85,
        },
        "calm": {
            "pace": 0.9,
            "temperature": 0.6,
        },
        "surprised": {
            "pace": 1.1,
            "temperature": 0.9,
        },
    }

    STYLE_MAP = {
        "energetic": {
            "pace": 1.1,
            "temperature": 0.85,
        },
        "soft": {
            "pace": 0.9,
        },
        "gentle": {
            "pace": 0.92,
        },
        "strong": {
            "pace": 1.05,
            "temperature": 0.8,
        },
        "shaky": {
            "pace": 1.08,
            "temperature": 0.9,
        },
        "cheerful": {
            "pace": 1.05,
            "temperature": 0.8,
        },
        "dramatic": {
            "temperature": 0.9,
        },
    }

    SPEED_MAP = {
        "very_slow": 0.75,
        "slow": 0.88,
        "normal": 1.0,
        "fast": 1.12,
        "very_fast": 1.25,
    }

    def build(
        self,
        emotion="happy",
        voice_style="",
        speaking_speed="",
    ):

        performance = dict(
            self.DEFAULTS
        )

        emotion_key = (
            str(emotion or "")
            .strip()
            .lower()
        )

        performance.update(
            self.EMOTION_MAP.get(
                emotion_key,
                {},
            )
        )

        style_key = (
            str(voice_style or "")
            .strip()
            .lower()
        )

        performance.update(
            self.STYLE_MAP.get(
                style_key,
                {},
            )
        )

        speed_key = (
            str(speaking_speed or "")
            .strip()
            .lower()
        )

        if speed_key in self.SPEED_MAP:

            performance["pace"] = (
                self.SPEED_MAP[
                    speed_key
                ]
            )

        return performance