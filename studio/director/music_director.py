class MusicDirector:
    """
    Music Director

    Selects background music based on
    scene emotion and story context.
    """

    EMOTION_MUSIC = {

        "happy": "happy_adventure",

        "excited": "heroic_adventure",

        "worried": "soft_suspense",

        "sad": "gentle_emotional",

        "scared": "danger_suspense",

        "angry": "intense_action",

        "surprised": "mystery",

        "celebration": "victory",

        "proud": "inspiring"
    }

    def process(self, story):

        for scene in story.scenes:

            if scene.music:
                continue

            scene.music = self.choose_music(scene)

        return story

    def choose_music(self, scene):

        for dialogue in scene.dialogues:

            emotion = (
                dialogue.emotion.lower()
                if dialogue.emotion
                else ""
            )

            if emotion in self.EMOTION_MUSIC:

                return self.EMOTION_MUSIC[emotion]

        return "happy_adventure"