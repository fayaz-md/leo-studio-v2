import json
import re
from datetime import datetime
from pathlib import Path


def slugify(text):

    text = text.strip()

    text = text.replace(" ", "_")

    text = re.sub(r"[^\w]", "_", text)

    while "__" in text:
        text = text.replace("__", "_")

    return text[:50]


def create_project(title, projects_dir):

    folder_name = slugify(title)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    project = projects_dir / f"{folder_name}_{timestamp}"

    project.mkdir(
        parents=True,
        exist_ok=True,
    )

    (project / "images").mkdir(exist_ok=True)

    (project / "audio").mkdir(exist_ok=True)

    return project


def save_json(path, data):

    with open(path, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4,
        )


def save_text(path, text):

    with open(path, "w", encoding="utf-8") as f:

        f.write(text)