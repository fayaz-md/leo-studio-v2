"""
Leo Studio Negative Prompt Builder

Builds a reusable negative prompt
to improve AI image quality.
"""


class NegativePromptBuilder:

    def __init__(self):

        self.negative_tags = [

            "no text",

            "no watermark",

            "no logo",

            "no signature",

            "no border",

            "no frame",

            "no blurry image",

            "no low quality",

            "no pixelation",

            "no duplicate characters",

            "no extra limbs",

            "no extra arms",

            "no extra legs",

            "no cropped characters",

            "no deformed face",

            "no distorted anatomy",

            "no floating objects",

            "no bad hands",

            "no bad eyes",

            "no artifacts",

        ]

    def build(self):

        return ", ".join(self.negative_tags)