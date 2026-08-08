"""
Leo Studio

Dialogue Validator

Checks whether dialogue stays
consistent with each character.
"""


class DialogueValidator:

    def validate(
        self,
        dialogue,
        character,
    ):

        issues = []

        text = dialogue.text.lower()

        character_id = character.id.lower()

        # -----------------------------------------
        # Leo
        # -----------------------------------------

        if character_id == "leo":

            if "analysis" in text:

                issues.append(
                    "Leo sounds too technical."
                )

        # -----------------------------------------
        # Meera
        # -----------------------------------------

        elif character_id == "meera":

            if "beep" in text:

                issues.append(
                    "Meera sounds robotic."
                )

        # -----------------------------------------
        # Robbie
        # -----------------------------------------

        elif character_id == "robbie":

            if "i am scared" in text:

                issues.append(
                    "Robbie became emotional."
                )

        return issues