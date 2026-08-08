"""
Leo Studio

Dialogue Brain

Validates generated dialogue without
rewriting the original text.
"""

from studio.brain.character_brain import CharacterBrain


class DialogueBrain:

    def __init__(self):

        self.character_brain = CharacterBrain()

    def improve(self, character, dialogue):

        info = self.character_brain.get_character(
            character
        )

        if not info:
            return dialogue

        dialogue = dialogue.strip()

        # -------------------------------------------------
        # Validate dialogue
        # -------------------------------------------------

        if not self.character_brain.validate_dialogue(
            character,
            dialogue,
        ):

            print(
                f"[Dialogue Warning] "
                f"{character}: "
                f"dialogue contains a forbidden phrase."
            )

        # -------------------------------------------------
        # Preserve original dialogue
        # -------------------------------------------------

        return dialogue