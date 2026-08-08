"""
Leo Studio Camera Director

Chooses the most cinematic camera angle
based on scene emotion first, then dialogue
actions and emotions.
"""


class CameraDirector:

    ACTION_CAMERA = {

        "runs": "tracking shot",

        "running": "tracking shot",

        "points": "close-up",

        "pointing": "close-up",

        "discovers": "medium close-up",

        "looks": "close-up",

        "talks": "medium shot",

        "celebrates": "wide shot",

        "laughs": "medium shot",

        "cries": "close-up",

        "jumps": "low angle",

        "flies": "wide aerial shot",

    }

    EMOTION_CAMERA = {

        "excited": "dynamic close-up",

        "worried": "close-up",

        "sad": "close-up",

        "happy": "medium shot",

        "surprised": "zoom-in",

        "scared": "low angle",

        "angry": "low angle",

    }

    SCENE_CAMERA = {

        "danger": "extreme close-up, shaky handheld",

        "worry": "slow push-in close-up",

        "thinking": "eye-level medium shot",

        "discovery": "cinematic dolly-in",

        "victory": "hero wide shot",

        "celebration": "wide aerial shot",

        "learning": "medium close-up",

    }

    def process(self, story):

        for scene in story.scenes:

            if scene.camera:
                continue

            scene.camera = self.choose_camera(
                scene
            )

        return story

    def choose_camera(self, scene):

        # ---------------------------------------------
        # Highest priority:
        # Emotion assigned by Emotion Pipeline
        # ---------------------------------------------

        scene_emotion = getattr(
            scene,
            "emotion",
            "",
        )

        if scene_emotion in self.SCENE_CAMERA:

            return self.SCENE_CAMERA[
                scene_emotion
            ]

        # ---------------------------------------------
        # Character actions
        # ---------------------------------------------

        for dialogue in scene.dialogues:

            action = (
                dialogue.action.lower()
                if dialogue.action
                else ""
            )

            for key, value in self.ACTION_CAMERA.items():

                if key in action:

                    return value

        # ---------------------------------------------
        # Character emotions
        # ---------------------------------------------

        for dialogue in scene.dialogues:

            emotion = (
                dialogue.emotion.lower()
                if dialogue.emotion
                else ""
            )

            if emotion in self.EMOTION_CAMERA:

                return self.EMOTION_CAMERA[
                    emotion
                ]

        # ---------------------------------------------
        # Default
        # ---------------------------------------------

        return "medium shot"