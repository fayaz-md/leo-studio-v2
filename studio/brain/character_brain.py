"""
Leo Studio Character Brain
"""


class CharacterBrain:

    def __init__(self):

        self.characters = {

            "leo": {

                "traits": {

                    "bravery": 10,
                    "kindness": 10,
                    "curiosity": 10,
                    "leadership": 9,
                    "humor": 8,
                    "creativity": 9,
                },

                "favorite_phrases": [

                    "I've got an idea!",

                    "Let's help together!",

                    "Awesome!",

                    "Don't worry!",

                    "We can do this!",

                ],

                "never_says": [

                    "I give up.",

                    "I don't care.",

                    "Let's run away.",

                    "Someone else can do it.",

                ],

                "always_does": [

                    "Helps friends",

                    "Protects animals",

                    "Encourages others",

                    "Finds creative solutions",

                ],

            },

            "meera": {

                "traits": {

                    "intelligence": 10,
                    "logic": 10,
                    "kindness": 9,
                    "patience": 9,
                    "curiosity": 8,
                },

                "favorite_phrases": [

                    "Let's think about it.",

                    "Science can help.",

                    "Wait... I have an idea.",

                ],

            },

            "robbie": {

                "traits": {

                    "logic": 10,
                    "precision": 10,
                    "helpfulness": 10,
                    "humor": 7,
                },

                "favorite_phrases": [

                    "Scanning...",

                    "Analysis complete.",

                    "Mission accepted.",

                    "Warning detected!",

                ],

            },

        }

    def get_character(
        self,
        name,
    ):

        return self.characters.get(
            name.lower()
        )

    def favorite_phrase(
        self,
        name,
    ):

        character = self.get_character(
            name
        )

        if not character:
            return None

        phrases = character.get(
            "favorite_phrases",
            []
        )

        if not phrases:
            return None

        return phrases[0]

    def validate_dialogue(
        self,
        character_name,
        text,
    ):

        character = self.get_character(
            character_name
        )

        if not character:
            return True

        for sentence in character.get(
            "never_says",
            [],
        ):

            if sentence.lower() in text.lower():

                return False

        return True