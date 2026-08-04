from studio.config import (
    DEFAULT_IMAGE_STYLE,
    DEFAULT_ASPECT_RATIO,
)


class PromptBuilder:

    def __init__(self):

        self.quality_prompt = (
            "cinematic lighting, "
            "3D animated movie, "
            "highly detailed, "
            "masterpiece quality, "
            "family friendly, "
            "vibrant colors"
        )

    def build(self, scene, characters):

        prompt_parts = []

        # --------------------------------------------------
        # Style
        # --------------------------------------------------

        prompt_parts.append(
            f"{DEFAULT_IMAGE_STYLE} style"
        )

        prompt_parts.append(
            f"Vertical {DEFAULT_ASPECT_RATIO}"
        )

        # --------------------------------------------------
        # Characters
        # --------------------------------------------------

        for character in characters:

            appearance = character.appearance

            description = ", ".join(
                value
                for value in appearance.values()
                if value
            )

            prompt_parts.append(description)

        # --------------------------------------------------
        # Scene
        # --------------------------------------------------

        prompt_parts.append(scene.image_prompt)

        # --------------------------------------------------
        # Camera
        # --------------------------------------------------

        if scene.camera:

            prompt_parts.append(
                f"Camera: {scene.camera}"
            )

        # --------------------------------------------------
        # Quality
        # --------------------------------------------------

        prompt_parts.append(self.quality_prompt)

        return ", ".join(prompt_parts)