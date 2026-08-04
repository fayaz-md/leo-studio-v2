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
            "display_name": character.display_name,
            "species": character.species,
            "gender": character.gender,
            "age": character.age,
            "role": character.role,
            "voice_profile": character.voice_profile,
            "personality": character.personality,
            "appearance": character.appearance,
            "relationships": character.relationships,
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

    def get(self, character_id):

        if not self.exists(character_id):
            return None

        return self.load(character_id)

    def get_characters_for_scene(self, scene):

        scene_text = " ".join([
            scene.title,
            scene.narration,
            " ".join(
                dialogue.speaker
                for dialogue in scene.dialogues
            ),
        ]).lower()

        matched = []

        for character in self.all():

            names = {
                character.id.lower(),
                character.display_name.lower(),
            }

            if any(name in scene_text for name in names):
                matched.append(character)

        return matched