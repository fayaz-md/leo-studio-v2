"""
Leo Studio Cinematic Prompt Builder
"""

from studio.prompt.camera_builder import CameraBuilder
from studio.prompt.lighting_builder import LightingBuilder
from studio.prompt.composition_builder import CompositionBuilder
from studio.prompt.negative_prompt_builder import NegativePromptBuilder


class CinematicPromptBuilder:

    def __init__(self):

        self.camera = CameraBuilder()

        self.lighting = LightingBuilder()

        self.composition = CompositionBuilder()

        self.negative = NegativePromptBuilder()

    def build(
        self,
        scene,
    ):

        prompt = []

        # -------------------------------------------------
        # Base Quality
        # -------------------------------------------------

        prompt.append(
            "Pixar-quality 3D animation"
        )

        prompt.append(
            "masterpiece"
        )

        prompt.append(
            "highly detailed"
        )

        prompt.append(
            "cinematic"
        )

        prompt.append(
            "family friendly"
        )

        prompt.append(
            "vertical 9:16"
        )

        # -------------------------------------------------
        # Scene Prompt
        # -------------------------------------------------

        prompt.append(
            scene.final_image_prompt
            or
            scene.image_prompt
        )

        # -------------------------------------------------
        # Camera
        # -------------------------------------------------

        prompt.append(

            self.camera.build(
                scene
            )

        )

        # -------------------------------------------------
        # Lighting
        # -------------------------------------------------

        prompt.append(

            self.lighting.build(
                scene
            )

        )

        # -------------------------------------------------
        # Composition
        # -------------------------------------------------

        prompt.append(

            self.composition.build(
                scene
            )

        )

        # -------------------------------------------------
        # Negative Prompt
        # -------------------------------------------------

        prompt.append(

            self.negative.build()

        )

        return ", ".join(prompt)