"""
Leo Studio

Scene Audio Assembler

Combines character dialogue WAV files into
a single audio file for each scene while
respecting dialogue duration and pause_after timing.
"""

import json
import shutil
import subprocess
from pathlib import Path


class SceneAudioAssembler:

    def __init__(self):

        self.ffmpeg = shutil.which(
            "ffmpeg"
        )

        self.ffprobe = shutil.which(
            "ffprobe"
        )

        if not self.ffmpeg:

            raise RuntimeError(
                "FFmpeg not found. "
                "Please install FFmpeg and "
                "add it to PATH."
            )

        if not self.ffprobe:

            raise RuntimeError(
                "FFprobe not found. "
                "Please install FFmpeg and "
                "add it to PATH."
            )

    def assemble(
        self,
        dialogues,
        audio_files,
        output_file,
    ):

        if not dialogues:

            raise ValueError(
                "Dialogues are required."
            )

        if not audio_files:

            raise ValueError(
                "Audio files are required."
            )

        output_file = Path(
            output_file
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        inputs = []

        for dialogue in dialogues:

            speaker = (
                dialogue.speaker.lower()
            )

            audio_file = audio_files.get(
                speaker
            )

            if not audio_file:

                raise FileNotFoundError(
                    f"No audio file found "
                    f"for speaker: {speaker}"
                )

            audio_file = Path(
                audio_file
            )

            if not audio_file.exists():

                raise FileNotFoundError(
                    f"Audio file not found: "
                    f"{audio_file}"
                )

            inputs.append(
                audio_file
            )

        command = [
            self.ffmpeg,
            "-y",
        ]

        for audio_file in inputs:

            command.extend(
                [
                    "-i",
                    str(audio_file),
                ]
            )

        filter_parts = []

        current_start = 0.0

        for index, dialogue in enumerate(
            dialogues
        ):

            delay_ms = int(
                current_start * 1000
            )

            filter_parts.append(
                f"[{index}:a]"
                f"adelay={delay_ms}|"
                f"{delay_ms}"
                f"[a{index}]"
            )

            duration = self._get_duration(
                inputs[index]
            )

            pause_after = float(
                getattr(
                    dialogue,
                    "pause_after",
                    0.0,
                )
                or 0.0
            )

            current_start += (
                duration
                + pause_after
            )

        mixed_inputs = "".join(
            f"[a{index}]"
            for index in range(
                len(inputs)
            )
        )

        filter_complex = (
            ";".join(filter_parts)
            + ";"
            + mixed_inputs
            + f"amix=inputs={len(inputs)}:"
              "duration=longest:"
              "dropout_transition=0"
              "[out]"
        )

        command.extend(
            [
                "-filter_complex",
                filter_complex,
                "-map",
                "[out]",
                "-c:a",
                "pcm_s16le",
                str(output_file),
            ]
        )

        self._run_ffmpeg(
            command
        )

        return output_file

    def _get_duration(
        self,
        audio_file,
    ):

        command = [
            self.ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(audio_file),
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:

            raise RuntimeError(
                "\n".join(
                    [
                        "FFprobe Duration Check Failed",
                        "",
                        result.stderr,
                    ]
                )
            )

        try:

            data = json.loads(
                result.stdout
            )

            duration = float(
                data["format"]["duration"]
            )

        except (
            KeyError,
            TypeError,
            ValueError,
            json.JSONDecodeError,
        ) as exc:

            raise RuntimeError(
                "Unable to determine "
                f"audio duration: {audio_file}"
            ) from exc

        return duration

    def _run_ffmpeg(
        self,
        command,
    ):

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:

            raise RuntimeError(
                "\n".join(
                    [
                        "Scene Audio Assembly Failed",
                        "",
                        result.stderr,
                    ]
                )
            )