"""
Leo Studio Provider Registry
"""


class Registry:

    def __init__(self):

        self.story_providers = {}

        self.image_providers = {}

        self.voice_providers = {}

        self.video_providers = {}

        self.music_providers = {}

    # =====================================================
    # Story Providers
    # =====================================================

    def register_story_provider(
        self,
        name,
        provider,
    ):

        self.story_providers[name] = provider

    def get_story_provider(
        self,
        name,
    ):

        return self.story_providers.get(name)

    # =====================================================
    # Image Providers
    # =====================================================

    def register_image_provider(
        self,
        name,
        provider,
    ):

        self.image_providers[name] = provider

    def get_image_provider(
        self,
        name,
    ):

        return self.image_providers.get(name)

    # =====================================================
    # Voice Providers
    # =====================================================

    def register_voice_provider(
        self,
        name,
        provider,
    ):

        self.voice_providers[name] = provider

    def get_voice_provider(
        self,
        name,
    ):

        return self.voice_providers.get(name)

    # =====================================================
    # Video Providers
    # =====================================================

    def register_video_provider(
        self,
        name,
        provider,
    ):

        self.video_providers[name] = provider

    def get_video_provider(
        self,
        name,
    ):

        return self.video_providers.get(name)

    # =====================================================
    # Music Providers
    # =====================================================

    def register_music_provider(
        self,
        name,
        provider,
    ):

        self.music_providers[name] = provider

    def get_music_provider(
        self,
        name,
    ):

        return self.music_providers.get(name)