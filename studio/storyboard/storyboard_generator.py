from studio.storyboard.storyboard_models import (
    Storyboard,
    StoryboardScene,
)


class StoryboardGenerator:

    def generate(
        self,
        story,
    ):

        storyboard = Storyboard(

            title=story.metadata.episode_title,

            duration=0,

        )

        total = 0

        for scene in story.scenes:

            board_scene = StoryboardScene(

                scene_number=scene.number,

                title=scene.title,

                duration=scene.duration,

                emotion=scene.emotion,

                camera=scene.camera,

                lighting="Auto",

                animation=scene.animation_prompt,

                music=scene.music,

                sfx=scene.sfx,

                narration=scene.narration,

                dialogues=scene.dialogues,

                image_prompt=scene.final_image_prompt,

                transition="Cut",

            )

            storyboard.scenes.append(
                board_scene
            )

            total += scene.duration

        storyboard.duration = total

        return storyboard