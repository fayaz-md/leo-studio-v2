from pathlib import Path

from studio.voice_manager import VoiceManager
from studio.providers.edge_provider import EdgeProvider


class VoiceGenerator:

    def __init__(self, assets_folder):

        self.voice_manager = VoiceManager(assets_folder)

        self.provider = EdgeProvider()

    def generate_project(self, story, project_folder):

        audio_folder = Path(project_folder) / "audio"

        audio_folder.mkdir(exist_ok=True)

        print()

        print("Generating voices...")

        print()

        for scene in story["scenes"]:

            filename = audio_folder / f"scene_{scene['number']:03}.mp3"

            settings = self.voice_manager.get_voice_settings(
                "leo",
                "happy",
            )

            self.provider.generate(
                text=scene["narration"],
                voice=settings["voice"],
                rate=settings["rate"],
                pitch=settings["pitch"],
                volume=settings["volume"],
                output_file=str(filename),
            )

            print(f"✅ Scene {scene['number']} complete")