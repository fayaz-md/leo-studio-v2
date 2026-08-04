import json
from pathlib import Path

from studio.models import Character


class CharacterManager:

    def __init__(self, assets_folder):

        self.characters_folder = Path(assets_folder) / "characters"

        self.characters_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _file(self, character_id):

        return self.characters_folder / f"{character_id}.json"

    def exists(self, character_id):

        return self._file(character_id).exists()

    def save(self, character: Character):

        data = {
            "id": character.id,
            "name": character.name,
            "species": character.species,
            "gender": character.gender,
            "age": character.age,
            "role": character.role,
            "voice": character.voice,
            "personality": character.personality,
            "catchphrase": character.catchphrase,
            "default_emotion": character.default_emotion,
        }

        with open(self._file(character.id), "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4,
            )

    def load(self, character_id):

        with open(self._file(character_id), "r", encoding="utf-8") as f:

            data = json.load(f)

        return Character(**data)

    def all(self):

        characters = []

        for file in self.characters_folder.glob("*.json"):

            characters.append(
                self.load(file.stem)
            )

        return characters