"""
Leo Studio Emotion Brain
"""


class EmotionBrain:

    def __init__(self):

        self.story_arc = [

            "danger",

            "worry",

            "thinking",

            "discovery",

            "victory",

            "celebration",

            "learning",

        ]

        self.scene_music = {

            "danger": "suspense",

            "worry": "soft_tension",

            "thinking": "curious",

            "discovery": "hope",

            "victory": "heroic",

            "celebration": "happy",

            "learning": "inspiring",

        }

    # -------------------------------------------------

    def emotion_for_scene(
        self,
        scene_number,
    ):

        index = min(
            scene_number - 1,
            len(self.story_arc) - 1,
        )

        return self.story_arc[index]

    # -------------------------------------------------

    def music_for_scene(
        self,
        scene_number,
    ):

        emotion = self.emotion_for_scene(
            scene_number
        )

        return self.scene_music.get(
            emotion,
            "happy",
        )