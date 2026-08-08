"""
Leo Studio

Workflow Pipeline

Coordinates the production stages that operate
on an already processed Story.
"""

from studio.pipelines.voice_pipeline import (
    VoicePipeline,
)


class WorkflowPipeline:

    def __init__(self):

        self.voice_pipeline = (
            VoicePipeline()
        )

    def process(self, story):

        if not story:

            raise ValueError(
                "Story is required."
            )

        voice_results = (
            self.voice_pipeline.process(
                story
            )
        )

        return {
            "story": story,
            "voice_results": voice_results,
        }