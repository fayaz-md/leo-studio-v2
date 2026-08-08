from dataclasses import dataclass, field


# =====================================================
# Scene Analysis
# =====================================================

@dataclass
class SceneAnalysis:

    scene_number: int

    hook_score: int = 0

    dialogue_score: int = 0

    emotion_score: int = 0

    visual_score: int = 0

    education_score: int = 0

    retention_score: int = 0

    youtube_score: int = 0

    comments: list[str] = field(
        default_factory=list
    )


# =====================================================
# Story Analysis
# =====================================================

@dataclass
class StoryAnalysis:

    overall_score: int = 0

    hook_score: int = 0

    dialogue_score: int = 0

    emotion_score: int = 0

    visual_score: int = 0

    education_score: int = 0

    retention_score: int = 0

    youtube_score: int = 0

    character_score: int = 0

    scene_flow_score: int = 0

    scenes: list[SceneAnalysis] = field(
        default_factory=list
    )

    comments: list[str] = field(
        default_factory=list
    )