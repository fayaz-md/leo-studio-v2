import json
import re
import unicodedata
from pathlib import Path


class CharacterRegistry:
    """
    Persistent Character Registry.

    Every recurring character is stored under:

    assets/
        characters/
            <character>.json
    """

    def __init__(self, registry_path="assets/characters"):

        self.registry_path = Path(registry_path)
        self.registry_path.mkdir(parents=True, exist_ok=True)

    # -----------------------------------------------------
    # Utilities
    # -----------------------------------------------------

    def _normalize_name(self, name: str) -> str:

        name = unicodedata.normalize("NFKC", name.strip())

        name = name.lower()

        name = re.sub(r"[^\w\u0900-\u097f]+", "_", name)

        return name.strip("_")

    def _character_file(self, name: str) -> Path:

        return self.registry_path / f"{self._normalize_name(name)}.json"

    # -----------------------------------------------------
    # CRUD
    # -----------------------------------------------------

    def exists(self, name: str) -> bool:

        return self._character_file(name).exists()

    def load(self, name: str):

        file = self._character_file(name)

        if not file.exists():
            return None

        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, character: dict):

        file = self._character_file(
            character["display_name"]
        )

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                character,
                f,
                indent=4,
                ensure_ascii=False,
            )

    # -----------------------------------------------------
    # Registry
    # -----------------------------------------------------

    def create_if_missing(
        self,
        name,
        character_type="Unknown",
    ):

        existing = self.load(name)

        if existing:
            return existing

        character = {

            "id": self._normalize_name(name),

            "display_name": name,

            "species": character_type,

            "voice_profile": self._normalize_name(name),

            "appearance": {},

            "personality": {},

            "relationships": {},

            "locked": False,
        }

        self.save(character)

        return character

    def get_all(self):

        characters = []

        for file in sorted(self.registry_path.glob("*.json")):

            with open(file, "r", encoding="utf-8") as f:

                characters.append(json.load(f))

        return characters