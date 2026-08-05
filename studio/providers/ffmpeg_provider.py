import shutil
import subprocess
from pathlib import Path

from studio.providers.video_provider import VideoProvider


class FFmpegProvider(VideoProvider):

    def __init__(self):

        self.ffmpeg = shutil.which("ffmpeg")

        if not self.ffmpeg:
            raise RuntimeError(
                "FFmpeg not found. Please install FFmpeg and add it to PATH."
            )

    def render_scene(self, **kwargs):

        image_file = Path(kwargs["image_file"])
        audio_file = Path(kwargs["audio_file"])
        output_file = Path(kwargs["output_file"])

        duration = kwargs["duration"]

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        command = [

            self.ffmpeg,

            "-y",

            "-loop", "1",

            "-framerate", "30",

            "-i", str(image_file),

            "-i", str(audio_file),

            "-t", str(duration),

            "-c:v", "libx264",

            "-preset", "medium",

            "-pix_fmt", "yuv420p",

            "-c:a", "aac",

            "-b:a", "192k",

            "-movflags", "+faststart",

            "-shortest",

            str(output_file),
        ]

        print(f"Rendering {output_file.name}")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:

            raise RuntimeError(
                "\n".join(
                    [
                        "FFmpeg Scene Render Failed",
                        "",
                        result.stderr,
                    ]
                )
            )

        return output_file

    def merge_scenes(
        self,
        scene_files,
        output_file,
    ):

        output_file = Path(output_file)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        list_file = output_file.parent / "scenes.txt"

        with open(
            list_file,
            "w",
            encoding="utf-8",
        ) as f:

            for scene in scene_files:

                scene = Path(scene).resolve()

                f.write(
                    f"file '{scene.as_posix()}'\n"
                )

        command = [

            self.ffmpeg,

            "-y",

            "-f", "concat",

            "-safe", "0",

            "-i", str(list_file),

            "-c", "copy",

            str(output_file),
        ]

        print("Merging scene clips...")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:

            raise RuntimeError(
                "\n".join(
                    [
                        "FFmpeg Merge Failed",
                        "",
                        result.stderr,
                    ]
                )
            )

        try:
            list_file.unlink()
        except Exception:
            pass

        print()
        print("Video Created Successfully")
        print(output_file)

        return output_file