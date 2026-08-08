"""
Leo Studio Dialogue Pipeline
"""

from studio.brain.dialogue_brain import DialogueBrain

from studio.character_engine.character_engine import (
    CharacterEngine,
)


class DialoguePipeline:

    def __init__(self):

        self.brain = DialogueBrain()

        self.character_engine = (
            CharacterEngine()
        )

    def process(
        self,
        story,
    ):

        # -----------------------------------------
        # Dialogue Brain
        # -----------------------------------------

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

        # -----------------------------------------
        # Character Engine
        # -----------------------------------------

        story = self.character_engine.process(
            story
        )

        return story