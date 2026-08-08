import unittest

from studio.prompt.character_prompt_builder import (
    CharacterPromptBuilder,
)


class TestCharacterPromptBuilder(unittest.TestCase):

    def setUp(self):

        self.builder = CharacterPromptBuilder()

        self.characters = [

            {
                "id": "leo",
                "display_name": "Leo",
                "species": "Lion",
                "role": "Hero",
                "personality": {
                    "traits": [
                        "Brave",
                        "Helpful",
                        "Funny",
                    ]
                },
                "catchphrase": "Let's help!",
                "relationships": {
                    "friends": [
                        "meera",
                        "robbie",
                    ]
                },
            },

            {
                "id": "meera",
                "display_name": "Meera",
                "species": "Human",
                "role": "Scientist",
                "personality": {
                    "traits": [
                        "Smart",
                        "Calm",
                    ]
                },
                "catchphrase": "",
                "relationships": {
                    "friends": [
                        "leo",
                    ]
                },
            },

            {
                "id": "unknown",
                "display_name": "Unknown",
                "species": "Unknown",
                "role": "",
            },
        ]

    def test_builder_creates_character_rules(self):

        result = self.builder.build(
            self.characters
        )

        self.assertIn(
            "Character: Leo",
            result,
        )

        self.assertIn(
            "Character: Meera",
            result,
        )

    def test_personality_is_included(self):

        result = self.builder.build(
            self.characters
        )

        self.assertIn(
            "Brave",
            result,
        )

        self.assertIn(
            "Helpful",
            result,
        )

    def test_speech_style_is_included(self):

        result = self.builder.build(
            self.characters
        )

        self.assertIn(
            "Speech Style:",
            result,
        )

        self.assertIn(
            "Tone: friendly",
            result,
        )

    def test_relationships_are_included(self):

        result = self.builder.build(
            self.characters
        )

        self.assertIn(
            "Friends:",
            result,
        )

        self.assertIn(
            "meera",
            result,
        )

    def test_catchphrase_is_included(self):

        result = self.builder.build(
            self.characters
        )

        self.assertIn(
            "Catchphrase: Let's help!",
            result,
        )

    def test_incomplete_character_is_skipped(self):

        result = self.builder.build(
            self.characters
        )

        self.assertNotIn(
            "Character: Unknown",
            result,
        )


if __name__ == "__main__":
    unittest.main()