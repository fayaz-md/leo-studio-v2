from dataclasses import asdict
import json
from pathlib import Path

from studio.models import (
    Story,
    Metadata,
    Settings,
    Character,
    Scene,
    Dialogue,
)


class StorySerializer:

    @staticmethod
    def save(story: Story, output_file):

        output_file = Path(output_file)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(output_file, "w", encoding="utf-8") as f:

            json.dump(
                asdict(story),
                f,
                ensure_ascii=False,
                indent=4,
            )

    @staticmethod
    def load(input_file):

        input_file = Path(input_file)

        with open(input_file, "r", encoding="utf-8") as f:

            data = json.load(f)

        metadata = Metadata(**data["metadata"])

        settings = Settings(**data["settings"])

        characters = [
            Character(**c)
            for c in data.get("characters", [])
        ]

        scenes = []

        for scene in data.get("scenes", []):

            dialogues = [
                Dialogue(**d)
                for d in scene.get("dialogues", [])
            ]

            scene["dialogues"] = dialogues

            scenes.append(Scene(**scene))

        return Story(
            metadata=metadata,
            settings=settings,
            characters=characters,
            scenes=scenes,
        )