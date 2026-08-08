import json


class StoryboardWriter:

    def save(
        self,
        storyboard,
        path,
    ):

        output = {

            "title": storyboard.title,

            "duration": storyboard.duration,

            "scenes": [],

        }

        for scene in storyboard.scenes:

            output["scenes"].append({

                "scene": scene.scene_number,

                "title": scene.title,

                "duration": scene.duration,

                "emotion": scene.emotion,

                "camera": scene.camera,

                "lighting": scene.lighting,

                "animation": scene.animation,

                "music": scene.music,

                "sfx": scene.sfx,

                "narration": scene.narration,

                "image_prompt": scene.image_prompt,

                "transition": scene.transition,

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