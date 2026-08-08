from studio.image_prompt_builder import ImagePromptBuilder
from studio.prompt.cinematic_prompt_builder import (
    CinematicPromptBuilder,
)


class PromptPipeline:

    def __init__(self):

        self.image_prompt_builder = (
            ImagePromptBuilder()
        )

        self.cinematic_prompt_builder = (
            CinematicPromptBuilder()
        )

    def process(self, story):

        # -----------------------------------------
        # Existing prompt generation
        # -----------------------------------------

        story = self.image_prompt_builder.process(
            story
        )

        # -----------------------------------------
        # Cinematic Prompt Enhancement
        # -----------------------------------------

        for scene in story.scenes:

            scene.final_image_prompt = (
                self.cinematic_prompt_builder.build(
                    scene
                )
            )

        return story