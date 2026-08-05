from abc import ABC, abstractmethod


class VideoProvider(ABC):

    @abstractmethod
    def render_scene(self, **kwargs):
        """
        Render a single scene into a video clip.

        Expected kwargs:
            image_file
            audio_file
            output_file
            duration
            camera_effect
        """
        pass

    @abstractmethod
    def merge_scenes(
        self,
        scene_files,
        output_file,
    ):
        """
        Merge multiple scene clips into one final video.
        """
        pass