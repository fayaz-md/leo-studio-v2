"""
Leo Studio Timing Director

Determines scene duration, dialogue speed
and pause timing based on scene emotion.
"""


class TimingDirector:

    EMOTION_DURATION = {

        "danger": 4.0,

        "worry": 5.0,

        "thinking": 6.0,

        "discovery": 7.0,

        "victory": 6.0,

        "celebration": 5.0,

        "learning": 7.0,

    }

    EMOTION_SPEED = {

        "danger": "fast",

        "worry": "normal",

        "thinking": "slow",

        "discovery": "normal",

        "victory": "fast",

        "celebration": "fast",

        "learning": "slow",

    }

    def process(self, story):

        for scene in story.scenes:

            emotion = getattr(
                scene,
                "emotion",
                "learning",
            )

            duration = self.EMOTION_DURATION.get(
                emotion,
                6.0,
            )

            scene.duration = duration

            speed = self.EMOTION_SPEED.get(
                emotion,
                "normal",
            )

            for dialogue in scene.dialogues:

                dialogue.speaking_speed = speed

                if speed == "fast":

                    dialogue.pause_after = 0.2

                elif speed == "slow":

                    dialogue.pause_after = 0.6

                else:

                    dialogue.pause_after = 0.4

        return story