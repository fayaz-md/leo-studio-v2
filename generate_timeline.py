import json

from studio.config import PROJECTS_DIR
from studio.timeline import TimelineBuilder


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

    for index, project in enumerate(projects, start=1):

        print(f"{index}. {project.name}")

    print()

    choice = int(input("Select project: "))

    return projects[choice - 1]


def main():

    project = list_projects()

    if not project:
        return

    builder = TimelineBuilder()

    timeline = builder.build(project)

    timeline_data = {
        "total_duration": round(
            timeline.total_duration,
            2,
        ),
        "scenes": [
            {
                "scene_number": scene.scene_number,
                "image_file": scene.image_file,
                "audio_file": scene.audio_file,
                "duration": round(
                    scene.duration,
                    2,
                ),
                "transition": scene.transition,
                "camera_effect": scene.camera_effect,
            }
            for scene in timeline.scenes
        ],
    }

    with open(
        project / "timeline.json",
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            timeline_data,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print()
    print("✅ Timeline Generated")
    print()
    print(f"Scenes : {len(timeline.scenes)}")
    print(f"Duration : {timeline.total_duration:.2f} sec")
    print()
    print(project / "timeline.json")


if __name__ == "__main__":

    main()