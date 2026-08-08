"""
Leo Studio

Voice Pipeline

Converts processed story dialogue into
character-specific audio files.
"""

from pathlib import Path

from studio.voice_engine.voice_renderer import (
    VoiceRenderer,
)


class VoicePipeline:

    def __init__(self):

        self.renderer = VoiceRenderer()

    def process(
        self,
        story,
        output_dir="output/audio",
    ):

        if not story:
            raise ValueError(
                "Story is required."
            )

        output_directory = Path(
            output_dir
        )

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        results = []

        scene_number = 0

        for scene in story.scenes:

            scene_number += 1

            if not hasattr(
                scene,
                "dialogues",
            ):
                continue

            dialogue_number = 0

            for dialogue in scene.dialogues:

                if not dialogue.speaker:
                    continue

                if not dialogue.text:
                    continue

                dialogue_number += 1

                speaker = (
                    dialogue.speaker.lower()
                )

                filename = (
                    f"scene_"
                    f"{scene_number:02d}_"
                    f"{speaker}_"
                    f"{dialogue_number:03d}.wav"
                )

                output_path = (
                    output_directory
                    / filename
                )

                result = self.renderer.render(
                    {
                        "speaker": dialogue.speaker,
                        "text": dialogue.text,
                    },
                    str(output_path),
                )

                results.append(result)

        return results