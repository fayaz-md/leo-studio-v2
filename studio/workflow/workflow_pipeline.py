"""
Leo Studio

Workflow Pipeline

Coordinates the production stages that operate
on an already processed Story.
"""

from pathlib import Path

from studio.audio.scene_audio_assembler import (
    SceneAudioAssembler,
)

from studio.pipelines.video_pipeline import (
    VideoPipeline,
)

from studio.pipelines.voice_pipeline import (
    VoicePipeline,
)

from studio.timeline.timeline_generator import (
    TimelineGenerator,
)


class WorkflowPipeline:

    def __init__(self):

        self.voice_pipeline = (
            VoicePipeline()
        )

        self.timeline_generator = (
            TimelineGenerator()
        )

        self.scene_audio_assembler = (
            SceneAudioAssembler()
        )

        self.video_pipeline = (
            VideoPipeline()
        )

    def process(
        self,
        story,
        image_dir=None,
        audio_dir=None,
        output_file=None,
    ):

        if not story:

            raise ValueError(
                "Story is required."
            )

        voice_results = (
            self.voice_pipeline.process(
                story
            )
        )

        timeline = (
            self.timeline_generator.generate(
                story
            )
        )

        if (
            image_dir is None
            or audio_dir is None
            or output_file is None
        ):

            return {
                "story": story,
                "voice_results": voice_results,
                "timeline": timeline,
            }

        image_dir = Path(
            image_dir
        )

        audio_dir = Path(
            audio_dir
        )

        output_file = Path(
            output_file
        )

        audio_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        for scene in timeline.scenes:

            scene_number = (
                scene.scene_number
            )

            scene_audio_files = {}

            for result in voice_results:

                if result.get(
                    "scene"
                ) != scene_number:

                    continue

                speaker = result.get(
                    "speaker"
                )

                audio_file = result.get(
                    "audio_file"
                )

                if speaker and audio_file:

                    scene_audio_files[
                        speaker.lower()
                    ] = Path(
                        audio_file
                    )

            if not scene_audio_files:

                continue

            self.scene_audio_assembler.assemble(
                dialogues=scene.dialogues,
                audio_files=scene_audio_files,
                output_file=(
                    audio_dir
                    / (
                        f"scene_"
                        f"{scene_number:02d}.wav"
                    )
                ),
            )

        video_file = (
            self.video_pipeline.render(
                timeline=timeline,
                image_dir=image_dir,
                audio_dir=audio_dir,
                output_file=output_file,
            )
        )

        return {
            "story": story,
            "voice_results": voice_results,
            "timeline": timeline,
            "video_file": video_file,
        }