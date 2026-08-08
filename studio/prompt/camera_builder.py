"""
Leo Studio Camera Builder

Builds cinematic camera prompts
based on scene emotion.
"""


class CameraBuilder:

    CAMERA_BY_EMOTION = {

        "danger": [

            "extreme close-up",
            "shaky handheld camera",
            "dramatic low-angle shot",
            "cinematic action framing",

        ],

        "worry": [

            "close-up shot",
            "slow push-in",
            "eye-level framing",
            "cinematic emotional composition",

        ],

        "thinking": [

            "medium shot",
            "eye-level camera",
            "balanced composition",
            "calm cinematic framing",

        ],

        "discovery": [

            "cinematic dolly-in",
            "wide reveal shot",
            "dynamic perspective",
            "beautiful depth of field",

        ],

        "victory": [

            "hero shot",
            "epic wide-angle",
            "low-angle cinematic shot",
            "dramatic composition",

        ],

        "celebration": [

            "wide aerial shot",
            "group composition",
            "joyful cinematic framing",
            "dynamic camera",

        ],

        "learning": [

            "medium close-up",
            "eye-level educational framing",
            "friendly composition",

        ],

    }

    DEFAULT = [

        "medium cinematic shot",

        "eye-level",

        "Pixar movie framing",

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

        values = self.CAMERA_BY_EMOTION.get(
            emotion,
            self.DEFAULT,
        )

        return ", ".join(values)