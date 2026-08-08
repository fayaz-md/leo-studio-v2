"""
Leo Studio

Voice Renderer

Renders character dialogue into individual
audio files using the configured voice provider.
"""

from pathlib import Path

from studio.voice_engine.voice_assignment import (
    VoiceAssignment,
)
from studio.voice_engine.voice_performance import (
    VoicePerformance,
)
from studio.voice_engine.sarvam_provider import (
    SarvamProvider,
)


class VoiceRenderer:

    def __init__(self):

        self.voice_assignment = (
            VoiceAssignment()
        )

        self.voice_performance = (
            VoicePerformance()
        )

        self.provider = SarvamProvider()

    def render(
        self,
        dialogue,
        output_path,
    ):

        if not dialogue:

            raise ValueError(
                "Dialogue is required."
            )

        if not output_path:

            raise ValueError(
                "Output path is required."
            )

        assignment = (
            self.voice_assignment.assign(
                dialogue
            )
        )

        if not assignment:

            raise ValueError(
                "Unable to assign voice "
                "to dialogue speaker."
            )

        output_file = Path(
            output_path
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        text = dialogue.get(
            "text",
            "",
        )

        emotion = dialogue.get(
            "emotion",
            "happy",
        )

        voice_style = dialogue.get(
            "voice_style",
            "",
        )

        speaking_speed = dialogue.get(
            "speaking_speed",
            "",
        )

        pause_after = dialogue.get(
            "pause_after",
            0.0,
        )

        performance = (
            self.voice_performance.build(
                emotion=emotion,
                voice_style=voice_style,
                speaking_speed=speaking_speed,
            )
        )

        self.provider.synthesize(
            text=text,
            voice_profile=assignment[
                "voice_profile"
            ],
            output_path=str(
                output_file
            ),
            performance=performance,
        )

        return {
            "speaker": assignment[
                "speaker"
            ],
            "voice_id": assignment[
                "voice_id"
            ],
            "provider": assignment[
                "provider"
            ],
            "provider_voice_id": assignment[
                "provider_voice_id"
            ],
            "language_code": assignment[
                "language_code"
            ],
            "text": text,
            "emotion": emotion,
            "voice_style": voice_style,
            "speaking_speed": speaking_speed,
            "pause_after": pause_after,
            "performance": performance,
            "audio_path": str(
                output_file
            ),
        }