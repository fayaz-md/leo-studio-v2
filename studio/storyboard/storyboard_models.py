from dataclasses import dataclass, field


@dataclass
class StoryboardScene:

    scene_number: int

    title: str

    duration: float

    emotion: str

    camera: str

    lighting: str

    animation: str

    music: str

    sfx: str

    narration: str

    dialogues: list = field(
        default_factory=list
    )

    image_prompt: str = ""

    transition: str = ""


@dataclass
class Storyboard:

    title: str

    duration: float

    scenes: list[StoryboardScene] = field(
        default_factory=list
    )