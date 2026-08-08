"""
Leo Studio

Video Pipeline

Coordinates rendering of timeline scenes into
individual video clips and merges them into
a final video.
"""

from pathlib import Path

from studio.providers.ffmpeg_provider import (
    FFmpegProvider,
)


class VideoPipeline:

    def __init__(self):

        self.video_provider = (
            FFmpegProvider()
        )

    def render(
        self,
        timeline,
        image_dir,
        audio_dir,
        output_file,
    ):

        if not timeline:

            raise ValueError(
                "Timeline is required."
            )

        if not timeline.scenes:

            raise ValueError(
                "Timeline contains no scenes."
            )

        image_dir = Path(
            image_dir
        )

        audio_dir = Path(
            audio_dir
        )

        output_file = Path(
            output_file
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        scene_files = []

        for scene in timeline.scenes:

            scene_number = (
                scene.scene_number
            )

            image_file = (
                image_dir
                / f"scene_{scene_number:02d}.png"
            )

            audio_file = (
                audio_dir
                / f"scene_{scene_number:02d}.wav"
            )

            if not image_file.exists():

                raise FileNotFoundError(
                    "Scene image not found: "
                    f"{image_file}"
                )

            if not audio_file.exists():

                raise FileNotFoundError(
                    "Scene audio not found: "
                    f"{audio_file}"
                )

            scene_output = (
                output_file.parent
                / (
                    f"scene_"
                    f"{scene_number:02d}.mp4"
                )
            )

            self.video_provider.render_scene(
                image=image_file,
                audio=audio_file,
                output=scene_output,
                duration=scene.duration,
                camera_effect=scene.camera,
            )

            scene_files.append(
                scene_output
            )

        self.video_provider.merge_scenes(
            scene_files=scene_files,
            output=output_file,
        )

        return output_file