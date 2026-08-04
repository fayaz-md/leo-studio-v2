from pathlib import Path

from studio.character_manager import CharacterManager
from studio.config import ASSETS_DIR, PROJECTS_DIR
from studio.prompt_builder import PromptBuilder
from studio.serializer import StorySerializer


def list_projects():

    projects = sorted(
        [
            p for p in PROJECTS_DIR.iterdir()
            if p.is_dir()
        ]
    )

    if not projects:
        print("No projects found.")
        return None

    print()

    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project.name}")

    print()

    choice = int(input("Select project: "))

    return projects[choice - 1]


def main():

    project = list_projects()

    if not project:
        return

    story = StorySerializer.load(
        project / "story.json"
    )

    prompt_builder = PromptBuilder()

    character_manager = CharacterManager(
        ASSETS_DIR
    )

    prompts_folder = project / "prompts"

    prompts_folder.mkdir(
        exist_ok=True
    )

    print()
    print("Generating prompts...")
    print()

    for scene in story.scenes:

        characters = character_manager.get_characters_for_scene(
            scene
        )

        prompt = prompt_builder.build(
            scene,
            characters,
        )

        filename = (
            prompts_folder
            / f"scene_{scene.number:03}.txt"
        )

        filename.write_text(
            prompt,
            encoding="utf-8",
        )

        print(f"✅ Scene {scene.number}")

    print()
    print("Prompt generation complete.")
    print(prompts_folder)


if __name__ == "__main__":

    main()