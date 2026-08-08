"""
Leo Studio

Voice Engine

Coordinates voice assignment for dialogue.
"""

from studio.voice_engine.voice_assignment import (
    VoiceAssignment,
)


class VoiceEngine:

    def __init__(self):

        self.voice_assignment = (
            VoiceAssignment()
        )

    def process(self, dialogues):

        if not dialogues:
            return []

        results = []

        for dialogue in dialogues:

            assignment = (
                self.voice_assignment.assign(
                    dialogue
                )
            )

            if assignment:

                results.append(
                    {
                        "speaker": assignment[
                            "speaker"
                        ],
                        "text": dialogue.get(
                            "text",
                            "",
                        ),
                        "voice_id": assignment[
                            "voice_id"
                        ],
                        "character_id": assignment[
                            "character_id"
                        ],
                        "language": assignment[
                            "language"
                        ],
                        "voice_profile": assignment[
                            "voice_profile"
                        ],
                    }
                )

        return results