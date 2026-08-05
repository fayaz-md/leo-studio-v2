import json
from pathlib import Path

from studio.providers.ffmpeg_provider import FFmpegProvider
from studio.config import PROJECTS_DIR


def select_project():

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

    project = select_project()

    if project is None:
        return

    timeline_file = project / "timeline.json"

    if not timeline_file.exists():

        print("timeline.json not found.")
        return

    with open(
        timeline_file,
        "r",
        encoding="utf-8",
    ) as f:

        timeline = json.load(f)

    provider = FFmpegProvider()

    output_folder = project / "output"

    scenes_folder = output_folder / "scenes"

    scenes_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    rendered_scenes = []

    print()
    print("Rendering scenes...")
    print()

    for scene in timeline["scenes"]:

        output_file = (
            scenes_folder /
            f"scene_{scene['scene_number']:03d}.mp4"
        )

        provider.render_scene(

            image_file=scene["image_file"],

            audio_file=scene["audio_file"],

            output_file=output_file,

            duration=scene["duration"],

            camera_effect=scene["camera_effect"],
        )

        rendered_scenes.append(output_file)

    final_video = output_folder / "final_video.mp4"

    print()
    print("Creating final video...")
    print()

    provider.merge_scenes(
        rendered_scenes,
        final_video,
    )

    print()
    print("=" * 60)
    print("🎉 Leo Studio Render Complete")
    print("=" * 60)
    print()
    print(final_video)
    print()


if __name__ == "__main__":

    main()