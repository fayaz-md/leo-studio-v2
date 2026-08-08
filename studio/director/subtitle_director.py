class SubtitleDirector:
    """
    Subtitle Director

    Creates clean subtitles from dialogue.
    """

    def process(self, story):

        for scene in story.scenes:

            subtitles = []

            for dialogue in scene.dialogues:

                subtitles.append({

                    "speaker": dialogue.speaker,

                    "text": dialogue.text

                })

            scene.subtitles = subtitles

        return story