from collections import OrderedDict

from studio.character_registry import CharacterRegistry


class CharacterProcessor:
    """
    Character Processor

    Responsibilities
    ----------------
    - Detect characters used in a story
    - Create missing character profiles
    - Load existing character profiles
    - Return characters used in the episode
    """

    def __init__(self):

        self.registry = CharacterRegistry()

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def process_story(self, story):

        character_names = self.extract_character_names(story)

        characters = []

        for name in character_names:

            character = self.registry.create_if_missing(
                name=name,
                character_type=self.detect_type(name),
            )

            characters.append(character)

        return characters

    # --------------------------------------------------
    # Character Extraction
    # --------------------------------------------------

    def extract_character_names(self, story):

        names = OrderedDict()

        for scene in story.scenes:

            for dialogue in scene.dialogues:

                speaker = dialogue.speaker.strip()

                if not speaker:
                    continue

                if speaker.lower() == "narrator":
                    continue

                names[speaker] = True

        return list(names.keys())

    # --------------------------------------------------
    # Character Type Detection
    # --------------------------------------------------

    def detect_type(self, name):

        lookup = {

            "leo": "Lion",

            "meera": "Human",

            "priya": "Human",

            "robbie": "Robot",

            "robot": "Robot",
        }

        return lookup.get(
            name.lower(),
            "Unknown",
        )