from dataclasses import dataclass, field
from pathlib import Path
from mutagen.mp3 import MP3


@dataclass
class TimelineScene:

    scene_number: int

    image_file: str

    audio_file: str

    duration: float

    transition: str = "fade"

    camera_effect: str = "slow_zoom_in"


@dataclass
class Timeline:

    scenes: list[TimelineScene] = field(default_factory=list)

    total_duration: float = 0.0


class TimelineBuilder:

    def build(self, project_folder):

        project = Path(project_folder)

        timeline = Timeline()

        audio_folder = project / "audio"

        image_folder = project / "images"

        audio_files = sorted(audio_folder.glob("scene_*.mp3"))

        for audio in audio_files:

            scene_number = int(audio.stem.split("_")[1])

            image = image_folder / f"scene_{scene_number:03}.png"

            duration = MP3(audio).info.length

            timeline.scenes.append(

                TimelineScene(

                    scene_number=scene_number,

                    image_file=str(image),

                    audio_file=str(audio),

                    duration=duration,

                )

            )

        timeline.total_duration = sum(

            scene.duration

            for scene in timeline.scenes

        )

        return timeline