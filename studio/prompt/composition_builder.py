"""
Leo Studio Composition Builder

Builds cinematic composition prompts
based on scene emotion.
"""


class CompositionBuilder:

    COMPOSITION_BY_EMOTION = {

        "danger": [

            "rule of thirds",

            "dynamic composition",

            "foreground debris",

            "dramatic depth of field",

            "strong perspective",

        ],

        "worry": [

            "balanced framing",

            "soft depth of field",

            "subject centered",

            "emotional composition",

        ],

        "thinking": [

            "clean composition",

            "rule of thirds",

            "foreground and background separation",

            "natural framing",

        ],

        "discovery": [

            "cinematic reveal",

            "leading lines",

            "beautiful depth of field",

            "wide environmental composition",

        ],

        "victory": [

            "hero composition",

            "epic perspective",

            "dynamic foreground",

            "wide cinematic framing",

        ],

        "celebration": [

            "group composition",

            "colorful foreground",

            "joyful framing",

            "wide cinematic view",

        ],

        "learning": [

            "clean educational composition",

            "eye-level framing",

            "balanced layout",

            "clear subject focus",

        ],

    }

    DEFAULT = [

        "rule of thirds",

        "depth of field",

        "cinematic composition",

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

        values = self.COMPOSITION_BY_EMOTION.get(
            emotion,
            self.DEFAULT,
        )

        return ", ".join(values)