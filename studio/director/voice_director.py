class VoiceDirector:
    """
    Voice Director

    Converts character emotions into
    voice performance settings.

    This module enriches dialogue after
    the story has been generated.
    """

    EMOTION_MAP = {

        "happy": {
            "voice_style": "cheerful",
            "speaking_speed": "normal",
            "pause_after": 0.4,
        },

        "excited": {
            "voice_style": "energetic",
            "speaking_speed": "fast",
            "pause_after": 0.2,
        },

        "worried": {
            "voice_style": "soft",
            "speaking_speed": "slow",
            "pause_after": 0.6,
        },

        "sad": {
            "voice_style": "gentle",
            "speaking_speed": "slow",
            "pause_after": 0.8,
        },

        "angry": {
            "voice_style": "strong",
            "speaking_speed": "fast",
            "pause_after": 0.3,
        },

        "surprised": {
            "voice_style": "expressive",
            "speaking_speed": "fast",
            "pause_after": 0.2,
        },

        "scared": {
            "voice_style": "shaky",
            "speaking_speed": "fast",
            "pause_after": 0.2,
        }
    }

    def process(self, story):

        for scene in story.scenes:

            for dialogue in scene.dialogues:

                self.enrich(dialogue)

        return story

    def enrich(self, dialogue):

        emotion = (
            dialogue.emotion.lower()
            if dialogue.emotion
            else "happy"
        )

        settings = self.EMOTION_MAP.get(
            emotion,
            self.EMOTION_MAP["happy"]
        )

        dialogue.voice_style = settings["voice_style"]

        dialogue.speaking_speed = settings["speaking_speed"]

        dialogue.pause_after = settings["pause_after"]