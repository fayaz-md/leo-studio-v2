from studio.timeline.timeline_models import (
    Timeline,
    TimelineScene,
)


class TimelineGenerator:

    def generate(
        self,
        story,
    ):

        timeline = Timeline(
            total_duration=0
        )

        current_time = 0.0

        for scene in story.scenes:

            duration = getattr(
                scene,
                "duration",
                6.0,
            )

            timeline_scene = TimelineScene(

                scene_number=scene.number,

                title=scene.title,

                start_time=round(
                    current_time,
                    2,
                ),

                end_time=round(
                    current_time + duration,
                    2,
                ),

                duration=duration,

                emotion=getattr(
                    scene,
                    "emotion",
                    "",
                ),

                camera=getattr(
                    scene,
                    "camera",
                    "",
                ),

                animation=getattr(
                    scene,
                    "animation_prompt",
                    "",
                ),

                music=getattr(
                    scene,
                    "music",
                    "",
                ),

                sfx=getattr(
                    scene,
                    "sfx",
                    "",
                ),

                transition="Cut",

                image_prompt=getattr(
                    scene,
                    "final_image_prompt",
                    "",
                ),

                dialogues=getattr(
                    scene,
                    "dialogues",
                    [],
                ),

            )

            timeline.scenes.append(
                timeline_scene
            )

            current_time += duration

        timeline.total_duration = round(
            current_time,
            2,
        )

        return timeline