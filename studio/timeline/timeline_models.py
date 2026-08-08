from dataclasses import dataclass, field


@dataclass
class TimelineScene:

    scene_number: int

    title: str

    start_time: float

    end_time: float

    duration: float

    emotion: str

    camera: str

    animation: str

    music: str

    sfx: str

    transition: str

    image_prompt: str

    dialogues: list = field(
        default_factory=list
    )


@dataclass
class Timeline:

    total_duration: float

    scenes: list[TimelineScene] = field(
        default_factory=list
    )