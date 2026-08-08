"""
Leo Studio Animation Director

Chooses animation style based on scene emotion,
then dialogue actions and gestures.
"""


class AnimationDirector:

    ACTION_ANIMATION = {

        "runs": "fast run animation",

        "running": "fast run animation",

        "walks": "walk cycle",

        "walking": "walk cycle",

        "points": "point animation",

        "pointing": "point animation",

        "waves": "wave animation",

        "waving": "wave animation",

        "jumps": "jump animation",

        "jumping": "jump animation",

        "laughs": "laugh animation",

        "laughing": "laugh animation",

        "cries": "cry animation",

        "crying": "cry animation",

        "looks": "look around animation",

        "looking": "look around animation",

        "celebrates": "celebration animation",

        "celebrating": "celebration animation",

    }

    GESTURE_ANIMATION = {

        "raises one paw": "raise paw",

        "raises hand": "raise hand",

        "nods": "nod",

        "shakes head": "shake head",

        "claps": "clap",

        "shrugs": "shrug",

        "thumbs up": "thumbs up",

    }

    SCENE_ANIMATION = {

        "danger": "fast dramatic movement",

        "worry": "slow cautious movement",

        "thinking": "idle thinking animation",

        "discovery": "surprised reaction animation",

        "victory": "hero celebration animation",

        "celebration": "group celebration animation",

        "learning": "calm teaching animation",

    }

    def process(self, story):

        for scene in story.scenes:

            scene.animation_prompt = self.choose_animation(
                scene
            )

        return story

    def choose_animation(self, scene):

        # ---------------------------------------------
        # Scene Emotion
        # ---------------------------------------------

        scene_emotion = getattr(
            scene,
            "emotion",
            "",
        )

        if scene_emotion in self.SCENE_ANIMATION:

            return self.SCENE_ANIMATION[
                scene_emotion
            ]

        # ---------------------------------------------
        # Character Actions
        # ---------------------------------------------

        for dialogue in scene.dialogues:

            action = (
                dialogue.action.lower()
                if dialogue.action
                else ""
            )

            for key, value in self.ACTION_ANIMATION.items():

                if key in action:

                    return value

        # ---------------------------------------------
        # Character Gestures
        # ---------------------------------------------

        for dialogue in scene.dialogues:

            gesture = (
                dialogue.gesture.lower()
                if dialogue.gesture
                else ""
            )

            for key, value in self.GESTURE_ANIMATION.items():

                if key in gesture:

                    return value

        return "natural idle animation"