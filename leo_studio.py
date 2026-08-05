from studio.story import StoryGenerator
from studio.serializer import StorySerializer
from studio.utils import create_project, save_text
from studio.config import PROJECTS_DIR
from studio.character_processor import CharacterProcessor


def build_script(story):

    lines = []

    lines.append(f"# {story.metadata.episode_title}")
    lines.append("")

    for scene in story.scenes:

        lines.append(f"## Scene {scene.number} - {scene.title}")
        lines.append("")
        lines.append(f"**Narration:** {scene.narration}")
        lines.append("")

        for dialogue in scene.dialogues:

            lines.append(
                f"**{dialogue.speaker}:** {dialogue.text}"
            )

        lines.append("")
        lines.append(f"**Image Prompt:** {scene.image_prompt}")
        lines.append("")
        lines.append(f"**Animation Prompt:** {scene.animation_prompt}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def build_image_prompts(story):

    lines = []

    for scene in story.scenes:

        lines.append(f"# Scene {scene.number}")
        lines.append("")
        lines.append(scene.image_prompt)
        lines.append("")
        lines.append("=" * 60)
        lines.append("")

    return "\n".join(lines)


def main():

    print("=" * 60)
    print("🦁 Leo Studio V2")
    print("=" * 60)
    print()

    idea = input("Story Idea: ").strip()

    if not idea:
        print("Story idea cannot be empty.")
        return

    print()
    print("Generating story...")
    print()

    generator = StoryGenerator()

    story = generator.generate(idea)

    print("Processing characters...")

    character_processor = CharacterProcessor()

    characters = character_processor.process_story(story)

    print(f"Characters detected: {len(characters)}")

    for character in characters:
        print(f"  ✓ {character['display_name']} ({character['species']})")

    project = create_project(
        idea,
        PROJECTS_DIR,
    )

    StorySerializer.save(
        story,
        project / "story.json",
    )

    save_text(
        project / "script.md",
        build_script(story),
    )

    save_text(
        project / "image_prompts.md",
        build_image_prompts(story),
    )

    print()
    print("✅ Project Created")
    print()
    print(project)


if __name__ == "__main__":
    main()