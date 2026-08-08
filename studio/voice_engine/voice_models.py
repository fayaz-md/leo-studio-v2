"""
Leo Studio

Voice Models

Defines the unique voice identity for every
main character in Leo Studio.
"""


class VoiceModels:

    VOICES = {

        "leo": {

            "voice_id": "leo_v1",

            "character_id": "leo",

            "provider": "sarvam",

            "provider_voice_id": "shubh",

            "language_code": "hi-IN",

            "gender": "male",

            "age_style": "young",

            "pitch": "high",

            "speed": "energetic",

            "energy": "high",

            "tone": "warm",

            "emotion": "expressive",

            "style": "playful",

            "language": "Hindi",

            "description": (
                "Young male cartoon lion voice. "
                "Warm, energetic, playful and friendly. "
                "Expressive child-like delivery."
            ),

        },

        "meera": {

            "voice_id": "meera_v1",

            "character_id": "meera",

            "provider": "sarvam",

            "provider_voice_id": "priya",

            "language_code": "hi-IN",

            "gender": "female",

            "age_style": "young",

            "pitch": "medium_high",

            "speed": "medium",

            "energy": "calm",

            "tone": "clear",

            "emotion": "expressive",

            "style": "intelligent",

            "language": "Hindi",

            "description": (
                "Young female child voice. "
                "Clear, calm and intelligent with "
                "warm expressive delivery."
            ),

        },

        "robbie": {

            "voice_id": "robbie_v1",

            "character_id": "robbie",

            "provider": "sarvam",

            "provider_voice_id": "manan",

            "language_code": "hi-IN",

            "gender": "neutral",

            "age_style": "robotic",

            "pitch": "medium_high",

            "speed": "steady",

            "energy": "steady",

            "tone": "synthetic",

            "emotion": "expressive_robotic",

            "style": "analytical",

            "language": "Hindi",

            "description": (
                "Friendly futuristic robot voice. "
                "Slightly synthetic, precise and steady "
                "with playful robotic expression."
            ),

        },

    }

    @classmethod
    def get(cls, character_id):

        return cls.VOICES.get(
            character_id.lower()
        )

    @classmethod
    def exists(cls, character_id):

        return (
            character_id.lower()
            in cls.VOICES
        )