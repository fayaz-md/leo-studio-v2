import unittest

from studio.character_engine.dialogue_validator import (
    DialogueValidator,
)


class MockDialogue:

    def __init__(self, text):

        self.text = text


class MockCharacter:

    def __init__(
        self,
        character_id,
        display_name,
    ):

        self.id = character_id
        self.display_name = display_name


class TestDialogueValidator(unittest.TestCase):

    def setUp(self):

        self.validator = DialogueValidator()

    def test_normal_leo_dialogue(self):

        dialogue = MockDialogue(
            "Don't worry, we can save him!"
        )

        character = MockCharacter(
            "leo",
            "Leo",
        )

        issues = self.validator.validate(
            dialogue,
            character,
        )

        self.assertEqual(
            issues,
            [],
        )

    def test_leo_technical_dialogue(self):

        dialogue = MockDialogue(
            "The analysis shows a probability issue."
        )

        character = MockCharacter(
            "leo",
            "Leo",
        )

        issues = self.validator.validate(
            dialogue,
            character,
        )

        self.assertTrue(
            issues
        )

    def test_normal_meera_dialogue(self):

        dialogue = MockDialogue(
            "Science can help us solve this."
        )

        character = MockCharacter(
            "meera",
            "Meera",
        )

        issues = self.validator.validate(
            dialogue,
            character,
        )

        self.assertEqual(
            issues,
            [],
        )

    def test_meera_robotic_dialogue(self):

        dialogue = MockDialogue(
            "Beep! System activated."
        )

        character = MockCharacter(
            "meera",
            "Meera",
        )

        issues = self.validator.validate(
            dialogue,
            character,
        )

        self.assertTrue(
            issues
        )

    def test_normal_robbie_dialogue(self):

        dialogue = MockDialogue(
            "Scanning the area now."
        )

        character = MockCharacter(
            "robbie",
            "Robbie",
        )

        issues = self.validator.validate(
            dialogue,
            character,
        )

        self.assertEqual(
            issues,
            [],
        )

    def test_validator_does_not_modify_dialogue(self):

        original = (
            "We can save the baby elephant!"
        )

        dialogue = MockDialogue(
            original
        )

        character = MockCharacter(
            "leo",
            "Leo",
        )

        self.validator.validate(
            dialogue,
            character,
        )

        self.assertEqual(
            dialogue.text,
            original,
        )


if __name__ == "__main__":
    unittest.main()