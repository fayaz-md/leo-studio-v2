import json


class TimelineWriter:

    def save(
        self,
        timeline,
        path,
    ):

        output = {

            "total_duration": timeline.total_duration,

            "scenes": [],

        }

        for scene in timeline.scenes:

            output["scenes"].append({

                "scene": scene.scene_number,

                "title": scene.title,

                "start_time": scene.start_time,

                "end_time": scene.end_time,

                "duration": scene.duration,

                "emotion": scene.emotion,

                "camera": scene.camera,

                "animation": scene.animation,

                "music": scene.music,

                "sfx": scene.sfx,

                "transition": scene.transition,

                "image_prompt": scene.image_prompt,

                "dialogues": [

                    {

                        "speaker": d.speaker,

                        "text": d.text,

                    }

                    for d in scene.dialogues

                ]

            })

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                output,
                f,
                indent=4,
                ensure_ascii=False,
            )