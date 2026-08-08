import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

from studio.audio.scene_audio_assembler import (
    SceneAudioAssembler,
)


class TestSceneAudioAssembler(unittest.TestCase):

    def _create_audio_files(
        self,
        temp_dir,
    ):

        audio_files = {}

        for speaker in [
            "leo",
            "meera",
            "robbie",
        ]:

            audio_file = (
                temp_dir
                / f"{speaker}.wav"
            )

            audio_file.write_bytes(
                b"dummy audio"
            )

            audio_files[speaker] = (
                audio_file
            )

        return audio_files

    def test_assemble_scene_audio(self):

        dialogues = [
            SimpleNamespace(
                speaker="leo",
                pause_after=0.4,
            ),
            SimpleNamespace(
                speaker="meera",
                pause_after=0.6,
            ),
            SimpleNamespace(
                speaker="robbie",
                pause_after=0.2,
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:

            temp_dir = Path(temp_dir)

            audio_files = (
                self._create_audio_files(
                    temp_dir
                )
            )

            output_file = (
                temp_dir
                / "scene_01.wav"
            )

            assembler = (
                SceneAudioAssembler()
            )

            assembler._get_duration = (
                MagicMock(
                    side_effect=[
                        2.0,
                        1.5,
                        1.0,
                    ]
                )
            )

            assembler._run_ffmpeg = (
                MagicMock()
            )

            result = assembler.assemble(
                dialogues=dialogues,
                audio_files=audio_files,
                output_file=output_file,
            )

            self.assertEqual(
                result,
                output_file,
            )

            self.assertEqual(
                assembler._get_duration.call_count,
                3,
            )

            assembler._run_ffmpeg.assert_called_once()

    def test_pause_after_is_applied_using_duration(self):

        dialogues = [
            SimpleNamespace(
                speaker="leo",
                pause_after=0.4,
            ),
            SimpleNamespace(
                speaker="meera",
                pause_after=0.6,
            ),
            SimpleNamespace(
                speaker="robbie",
                pause_after=0.2,
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:

            temp_dir = Path(temp_dir)

            audio_files = (
                self._create_audio_files(
                    temp_dir
                )
            )

            output_file = (
                temp_dir
                / "scene_01.wav"
            )

            assembler = (
                SceneAudioAssembler()
            )

            assembler._get_duration = (
                MagicMock(
                    side_effect=[
                        2.0,
                        1.5,
                        1.0,
                    ]
                )
            )

            assembler._run_ffmpeg = (
                MagicMock()
            )

            assembler.assemble(
                dialogues=dialogues,
                audio_files=audio_files,
                output_file=output_file,
            )

            command = (
                assembler
                ._run_ffmpeg
                .call_args.args[0]
            )

            command_text = " ".join(
                str(value)
                for value in command
            )

            # Leo starts at 0.0 seconds.
            self.assertIn(
                "adelay=0|0",
                command_text,
            )

            # Meera starts after:
            # Leo duration 2.0
            # + Leo pause 0.4
            # = 2.4 seconds.
            self.assertIn(
                "adelay=2400|2400",
                command_text,
            )

            # Robbie starts after:
            # Leo duration 2.0
            # + Leo pause 0.4
            # + Meera duration 1.5
            # + Meera pause 0.6
            # = 4.5 seconds.
            self.assertIn(
                "adelay=4500|4500",
                command_text,
            )

    def test_missing_audio_file_raises_error(self):

        dialogues = [
            SimpleNamespace(
                speaker="leo",
                pause_after=0.4,
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:

            temp_dir = Path(temp_dir)

            missing_audio = (
                temp_dir
                / "leo.wav"
            )

            output_file = (
                temp_dir
                / "scene_01.wav"
            )

            assembler = (
                SceneAudioAssembler()
            )

            with self.assertRaises(
                FileNotFoundError
            ):

                assembler.assemble(
                    dialogues=dialogues,
                    audio_files={
                        "leo": missing_audio,
                    },
                    output_file=output_file,
                )

    def test_missing_speaker_audio_raises_error(self):

        dialogues = [
            SimpleNamespace(
                speaker="leo",
                pause_after=0.4,
            ),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:

            temp_dir = Path(temp_dir)

            output_file = (
                temp_dir
                / "scene_01.wav"
            )

            missing_audio = (
                temp_dir
                / "leo.wav"
            )

            assembler = (
                SceneAudioAssembler()
            )

            with self.assertRaises(
                FileNotFoundError
            ):

                assembler.assemble(
                    dialogues=dialogues,
                    audio_files={
                        "leo": missing_audio,
                    },
                    output_file=output_file,
                )


if __name__ == "__main__":
    unittest.main()