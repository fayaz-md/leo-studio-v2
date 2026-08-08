"""
Leo Studio Lighting Builder

Builds cinematic lighting prompts
based on scene emotion.
"""


class LightingBuilder:

    LIGHTING_BY_EMOTION = {

        "danger": [

            "dramatic cinematic lighting",

            "stormy atmosphere",

            "high contrast",

            "volumetric light rays",

            "intense shadows",

        ],

        "worry": [

            "soft cloudy daylight",

            "gentle ambient lighting",

            "slightly desaturated mood",

            "cinematic soft shadows",

        ],

        "thinking": [

            "warm natural daylight",

            "balanced soft lighting",

            "peaceful atmosphere",

            "clean illumination",

        ],

        "discovery": [

            "golden hour sunlight",

            "warm cinematic glow",

            "beautiful volumetric lighting",

            "sun rays through trees",

        ],

        "victory": [

            "bright heroic sunlight",

            "cinematic golden rim light",

            "vibrant colors",

            "epic lighting",

        ],

        "celebration": [

            "warm sunset lighting",

            "colorful festive atmosphere",

            "bright happy colors",

            "soft bloom",

        ],

        "learning": [

            "soft morning sunlight",

            "warm educational atmosphere",

            "pleasant natural lighting",

        ],

    }

    DEFAULT = [

        "natural daylight",

        "soft cinematic lighting",

    ]

    def build(
        self,
        scene,
    ):

        emotion = getattr(
            scene,
            "emotion",
            "",
        )

        values = self.LIGHTING_BY_EMOTION.get(
            emotion,
            self.DEFAULT,
        )

        return ", ".join(values)