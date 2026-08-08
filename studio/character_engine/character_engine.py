"""
Leo Studio

Character Engine

Coordinates character consistency
without rewriting generated dialogue.
"""

from studio.character_engine.dialogue_validator import (
    DialogueValidator,
)


class CharacterEngine:

    def __init__(self):

        self.validator = DialogueValidator()

    def process(
        self,
        story,
    ):

        character_map = {
            character.id.lower(): character
            for character in story.characters
        }

        for scene in story.scenes:

            for dialogue in scene.dialogues:

                if not dialogue.speaker:
                    continue

                character = character_map.get(
                    dialogue.speaker.lower()
                )

                if not character:
                    continue

                issues = self.validator.validate(
                    dialogue,
                    character,
                )

                if issues:

                    for issue in issues:

                        print(
                            f"[Character Warning] "
                            f"{character.display_name}: "
                            f"{issue}"
                        )

        return story