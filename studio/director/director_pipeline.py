from studio.director.voice_director import VoiceDirector
from studio.director.camera_director import CameraDirector
from studio.director.animation_director import AnimationDirector
from studio.director.music_director import MusicDirector
from studio.director.subtitle_director import SubtitleDirector


class DirectorPipeline:

    def __init__(self):

        self.directors = [

            VoiceDirector(),

            CameraDirector(),

            AnimationDirector(),

            MusicDirector(),

            SubtitleDirector(),

        ]

    def process(self, story):

        for director in self.directors:

            story = director.process(story)

        return story