import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from studio.workflow.workflow_pipeline import (
    WorkflowPipeline,
)


class TestWorkflowPipeline(unittest.TestCase):

    def test_process_runs_voice_pipeline(self):

        story = SimpleNamespace(
            scenes=[]
        )

        workflow = WorkflowPipeline()

        workflow.voice_pipeline = MagicMock()

        workflow.voice_pipeline.process.return_value = [
            {
                "speaker": "leo",
                "audio_path": "output/audio/leo.wav",
            }
        ]

        result = workflow.process(
            story
        )

        workflow.voice_pipeline.process.assert_called_once_with(
            story,
            output_dir="output/audio",
        )

        self.assertEqual(
            result["story"],
            story,
        )

        self.assertEqual(
            result["voice_results"],
            [
                {
                    "speaker": "leo",
                    "audio_path": (
                        "output/audio/leo.wav"
                    ),
                }
            ],
        )

    def test_process_preserves_story(self):

        story = SimpleNamespace(
            scenes=[]
        )

        workflow = WorkflowPipeline()

        workflow.voice_pipeline = MagicMock()

        workflow.voice_pipeline.process.return_value = []

        result = workflow.process(
            story
        )

        self.assertIs(
            result["story"],
            story,
        )

        self.assertEqual(
            result["voice_results"],
            [],
        )


if __name__ == "__main__":
    unittest.main()