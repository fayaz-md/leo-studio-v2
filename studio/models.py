from dataclasses import dataclass, field


# =====================================================
# Metadata
# =====================================================

@dataclass
class Metadata:

    project_name: str
    series: str
    episode: int
    episode_title: str
    language: str
    duration: int
    created_at: str
    generator: str
    version: str


# =====================================================
# Settings
# =====================================================

@dataclass
class Settings:

    story_provider: str
    voice_provider: str
    image_provider: str
    image_style: str
    aspect_ratio: str
    target_platform: str


# =====================================================
# Character
# =====================================================

@dataclass
class Character:

    id: str
    display_name: str

    species: str
    gender: str
    age: str
    role: str

    voice_profile: str

    personality: dict = field(default_factory=dict)
    appearance: dict = field(default_factory=dict)
    relationships: dict = field(default_factory=dict)

    catchphrase: str = ""
    default_emotion: str = "happy"

    locked: bool = False


# =====================================================
# Location
# =====================================================

@dataclass
class Location:

    id: str
    name: str
    description: str = ""


# =====================================================
# Prop
# =====================================================

@dataclass
class Prop:

    id: str
    name: str
    description: str = ""


# =====================================================
# Dialogue
# =====================================================

@dataclass
class Dialogue:

    # Identity
    speaker: str

    # Dialogue
    text: str

    # Emotion
    emotion: str = ""

    # Performance
    action: str = ""
    expression: str = ""
    pose: str = ""
    gesture: str = ""

    # Voice
    voice_style: str = ""
    speaking_speed: str = ""
    pause_after: float = 0.0

    # Camera
    camera_focus: str = ""


# =====================================================
# Scene
# =====================================================

@dataclass
class Scene:

    id: str

    number: int

    title: str

    narration: str

    image_prompt: str

    final_image_prompt: str = ""

    animation_prompt: str = ""

    camera: str = ""

    music: str = ""

    emotion: str = ""

    # NEW
    duration: float = 6.0

    sfx: str = ""

    dialogues: list[Dialogue] = field(
        default_factory=list
    )

    subtitles: list = field(
        default_factory=list
    )


# =====================================================
# Story
# =====================================================

@dataclass
class Story:

    metadata: Metadata

    settings: Settings

    characters: list[Character] = field(
        default_factory=list
    )

    locations: list[Location] = field(
        default_factory=list
    )

    props: list[Prop] = field(
        default_factory=list
    )

    scenes: list[Scene] = field(
        default_factory=list
    )