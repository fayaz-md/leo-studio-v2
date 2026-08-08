"""
Leo Studio Dialogue Pipeline
"""

from studio.brain.dialogue_brain import DialogueBrain


class DialoguePipeline:

    def __init__(self):

        self.brain = DialogueBrain()

    def process(
        self,
        story,
    ):

        for scene in story.scenes:

            if not hasattr(scene, "dialogues"):
                continue

            for dialogue in scene.dialogues:

                if not dialogue.speaker:
                    continue

                dialogue.text = self.brain.improve(
                    dialogue.speaker,
                    dialogue.text,
                )

        return story