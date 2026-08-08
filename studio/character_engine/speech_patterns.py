"""
Leo Studio Character Engine

Speech Pattern Engine

Defines the speaking style of each character.
"""


class SpeechPatterns:

    PATTERNS = {

        "leo": {

            "tone": "friendly",

            "sentence_length": "short",

            "energy": "high",

            "vocabulary": "simple",

            "style": "encouraging",

        },

        "meera": {

            "tone": "logical",

            "sentence_length": "medium",

            "energy": "calm",

            "vocabulary": "scientific",

            "style": "educational",

        },

        "robbie": {

            "tone": "robotic",

            "sentence_length": "short",

            "energy": "steady",

            "vocabulary": "technical",

            "style": "analytical",

        },

    }

    DEFAULT = {

        "tone": "neutral",

        "sentence_length": "medium",

        "energy": "normal",

        "vocabulary": "simple",

        "style": "friendly",

    }

    def get(
        self,
        character_id,
    ):

        return self.PATTERNS.get(

            character_id.lower(),

            self.DEFAULT,

        )