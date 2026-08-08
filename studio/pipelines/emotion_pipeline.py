"""
Leo Studio Emotion Pipeline
"""

from studio.brain.emotion_brain import EmotionBrain


class EmotionPipeline:

    def __init__(self):

        self.brain = EmotionBrain()

    def process(self, story):

        for scene in story.scenes:

            emotion = self.brain.emotion_for_scene(
                scene.number
            )

            scene.music = self.brain.music_for_scene(
                scene.number
            )

            # Store emotion on the scene so other
            # directors can use it.
            scene.emotion = emotion

        return story