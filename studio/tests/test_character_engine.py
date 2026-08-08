import unittest

from studio.character_engine.character_engine import (
    CharacterEngine,
)


class MockDialogue:

    def __init__(
        self,
        speaker,
        text,
    ):

        self.speaker = speaker
        self.text = text


class MockCharacter:

    def __init__(
        self,
        character_id,
        display_name,
    ):

        self.id = character_id
        self.display_name = display_name


class MockScene:

    def __init__(
        self,
        dialogues,
    ):

        self.dialogues = dialogues


class MockStory:

    def __init__(
        self,
        characters,
        scenes,
    ):

        self.characters = characters
        self.scenes = scenes


class TestCharacterEngine(unittest.TestCase):

    def setUp(self):

        self.engine = CharacterEngine()

        self.leo = MockCharacter(
            "leo",
            "Leo",
        )

        self.meera = MockCharacter(
            "meera",
            "Meera",
        )

    def test_engine_returns_story(self):

        dialogue = MockDialogue(
            "Leo",
            "Don't worry, we can save him!",
        )

        scene = MockScene(
            [dialogue]
        )

        story = MockStory(
            [self.leo],
            [scene],
        )

        result = self.engine.process(
            story
        )

        self.assertIs(
            result,
            story,
        )

    def test_valid_dialogue_is_unchanged(self):

        original = (
            "Don't worry, we can save him!"
        )

        dialogue = MockDialogue(
            "Leo",
            original,
        )

        scene = MockScene(
            [dialogue]
        )

        story = MockStory(
            [self.leo],
            [scene],
        )

        self.engine.process(
            story
        )

        self.assertEqual(
            dialogue.text,
            original,
        )

    def test_invalid_dialogue_is_not_rewritten(self):

        original = (
            "The analysis shows a probability issue."
        )

        dialogue = MockDialogue(
            "Leo",
            original,
        )

        scene = MockScene(
            [dialogue]
        )

        story = MockStory(
            [self.leo],
            [scene],
        )

        self.engine.process(
            story
        )

        self.assertEqual(
            dialogue.text,
            original,
        )

    def test_unknown_speaker_is_ignored(self):

        dialogue = MockDialogue(
            "Unknown",
            "Hello there!",
        )

        scene = MockScene(
            [dialogue]
        )

        story = MockStory(
            [self.leo],
            [scene],
        )

        result = self.engine.process(
            story
        )

        self.assertIs(
            result,
            story,
        )

        self.assertEqual(
            dialogue.text,
            "Hello there!",
        )


if __name__ == "__main__":
    unittest.main()