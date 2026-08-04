import json
from pathlib import Path


class VoiceManager:

    def __init__(self, assets_folder):

        self.assets = Path(assets_folder)

        self.voice_folder = self.assets / "voices"

        self.emotion_folder = self.assets / "emotions"

    def load_voice(self, voice_profile):

        file = self.voice_folder / f"{voice_profile}.json"

        with open(file, "r", encoding="utf-8") as f:

            return json.load(f)

    def load_emotion(self, emotion):

        file = self.emotion_folder / f"{emotion}.json"

        with open(file, "r", encoding="utf-8") as f:

            return json.load(f)

    def get_voice_settings(self, voice_profile, emotion):

        voice = self.load_voice(voice_profile)

        emo = self.load_emotion(emotion)

        return {

            "provider": voice["provider"],

            "voice": voice["voice"],

            "pitch": emo["pitch"],

            "rate": emo["rate"],

            "volume": emo["volume"]

        }