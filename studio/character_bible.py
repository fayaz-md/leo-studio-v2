import json
from pathlib import Path


class CharacterBible:

    def __init__(self, character_dir="assets/characters"):

        self.character_dir = Path(character_dir)

        self.characters = {}

    def load(self):

        self.characters.clear()

        if not self.character_dir.exists():
            return

        for file in self.character_dir.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:

                data = json.load(f)

            character_id = data.get("id")

            if character_id:

                self.characters[character_id.lower()] = data

    def get(self, character_id):

        if not character_id:
            return None

        return self.characters.get(
            character_id.lower()
        )

    def enrich(self, character):
        """
        Enrich an extracted character using the
        Character Bible.

        Character Bible values override extracted values
        when they are available.
        """

        if not character:
            return character

        character_id = character.get(
            "id",
            "",
        ).lower()

        bible_character = self.get(
            character_id
        )

        if not bible_character:
            return character

        enriched = character.copy()

        for key, value in bible_character.items():

            if value not in (
                "",
                None,
                [],
                {},
            ):
                enriched[key] = value

        return enriched

    def exists(self, character_id):

        if not character_id:
            return False

        return (
            character_id.lower()
            in self.characters
        )

    def all(self):

        return list(
            self.characters.values()
        )

    def count(self):

        return len(
            self.characters
        )