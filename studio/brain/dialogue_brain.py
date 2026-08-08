"""
Leo Studio Dialogue Brain
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
        # Remove forbidden dialogue
        # -------------------------------------------------

        if not self.character_brain.validate_dialogue(
            character,
            dialogue,
        ):

            phrase = self.character_brain.favorite_phrase(
                character
            )

            if phrase:
                return phrase

            return dialogue

        # -------------------------------------------------
        # Add signature opening
        # -------------------------------------------------

        phrase = self.character_brain.favorite_phrase(
            character
        )

        if phrase:

            if phrase.lower() not in dialogue.lower():

                if len(dialogue) < 60:

                    dialogue = (
                        phrase
                        + " "
                        + dialogue
                    )

        return dialogue