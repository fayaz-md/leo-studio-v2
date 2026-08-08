import unittest

from studio.brain.dialogue_brain import (
    DialogueBrain,
)


class TestDialogueBrain(unittest.TestCase):

    def setUp(self):

        self.brain = DialogueBrain()

    def test_dialogue_is_not_rewritten(self):

        original = (
            "बीप-बूप! खतरा! कोई बहुत बड़ी मुसीबत में है!"
        )

        result = self.brain.improve(
            "robbie",
            original,
        )

        self.assertEqual(
            result,
            original,
        )

    def test_meera_dialogue_is_not_rewritten(self):

        original = (
            "रुको लियो! ज़मीन बहुत गीली है!"
        )

        result = self.brain.improve(
            "meera",
            original,
        )

        self.assertEqual(
            result,
            original,
        )

    def test_leo_dialogue_is_not_rewritten(self):

        original = (
            "हमें उसकी मदद करनी होगी!"
        )

        result = self.brain.improve(
            "leo",
            original,
        )

        self.assertEqual(
            result,
            original,
        )

    def test_forbidden_dialogue_is_not_replaced(self):

        original = (
            "I give up."
        )

        result = self.brain.improve(
            "leo",
            original,
        )

        self.assertEqual(
            result,
            original,
        )


if __name__ == "__main__":
    unittest.main()