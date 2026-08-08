"""
Leo Studio Custom Exceptions
"""


class LeoStudioError(Exception):
    """Base exception for Leo Studio."""

    pass


# =====================================================
# Story
# =====================================================

class StoryGenerationError(LeoStudioError):

    pass


class StoryParsingError(LeoStudioError):

    pass


class StoryValidationError(LeoStudioError):

    pass


# =====================================================
# Prompt
# =====================================================

class PromptGenerationError(LeoStudioError):

    pass


# =====================================================
# Character
# =====================================================

class CharacterBibleError(LeoStudioError):

    pass


# =====================================================
# Image
# =====================================================

class ImageGenerationError(LeoStudioError):

    pass


# =====================================================
# Voice
# =====================================================

class VoiceGenerationError(LeoStudioError):

    pass


# =====================================================
# Timeline
# =====================================================

class TimelineError(LeoStudioError):

    pass


# =====================================================
# Video
# =====================================================

class VideoRenderingError(LeoStudioError):

    pass


# =====================================================
# Workflow
# =====================================================

class WorkflowError(LeoStudioError):

    pass