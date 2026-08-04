from pathlib import Path
import json

from studio.voice import VoiceGenerator


def choose_project():

    projects = sorted(Path("projects").iterdir())

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

    project = choose_project()

    if project is None:
        return

    story_file = project / "story.json"

    with open(story_file, "r", encoding="utf-8") as f:
        story = json.load(f)

    generator = VoiceGenerator("assets")

    generator.generate_project(
        story,
        project,
    )


if __name__ == "__main__":
    main()