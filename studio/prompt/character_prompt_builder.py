"""
Leo Studio

Character Prompt Builder

Builds prompt instructions for every
character before story generation.
"""

from studio.character_engine.speech_patterns import (
    SpeechPatterns,
)


class CharacterPromptBuilder:

    def __init__(self):

        self.speech_patterns = (
            SpeechPatterns()
        )

    def build(
        self,
        characters,
    ):

        sections = []

        sections.append(
            "=============================="
        )

        sections.append(
            "CHARACTER RULES"
        )

        sections.append(
            "==============================\n"
        )

        for character in characters:

            # -------------------------------------
            # Skip incomplete / duplicate entries
            # -------------------------------------

            if (
                not character.get("role")
                or character.get("species") in (
                    "",
                    "Unknown",
                )
            ):
                continue

            character_id = character.get(
                "id",
                "",
            )

            sections.append(
                f"Character: {character.get('display_name', '')}"
            )

            sections.append(
                f"Species: {character.get('species', '')}"
            )

            sections.append(
                f"Role: {character.get('role', '')}"
            )

            # -------------------------------------
            # Personality
            # -------------------------------------

            personality = character.get(
                "personality",
                {},
            )

            traits = personality.get(
                "traits",
                [],
            )

            if traits:

                sections.append(
                    "Traits:"
                )

                for trait in traits:

                    sections.append(
                        f"- {trait}"
                    )

            # -------------------------------------
            # Speech Pattern
            # -------------------------------------

            speech = self.speech_patterns.get(
                character_id
            )

            sections.append(
                "Speech Style:"
            )

            sections.append(
                f"- Tone: {speech['tone']}"
            )

            sections.append(
                f"- Sentence length: "
                f"{speech['sentence_length']}"
            )

            sections.append(
                f"- Energy: {speech['energy']}"
            )

            sections.append(
                f"- Vocabulary: "
                f"{speech['vocabulary']}"
            )

            sections.append(
                f"- Style: {speech['style']}"
            )

            # -------------------------------------
            # Relationships
            # -------------------------------------

            relationships = character.get(
                "relationships",
                {},
            )

            friends = relationships.get(
                "friends",
                [],
            )

            if friends:

                sections.append(
                    "Friends:"
                )

                for friend in friends:

                    sections.append(
                        f"- {friend}"
                    )

                sections.append(
                    "Treat these characters as friends "
                    "when they interact."
                )

            # -------------------------------------
            # Catchphrase
            # -------------------------------------

            catchphrase = character.get(
                "catchphrase",
                "",
            )

            if catchphrase:

                sections.append(
                    f"Catchphrase: {catchphrase}"
                )

                sections.append(
                    "Use occasionally and naturally."
                )

            # -------------------------------------
            # Character Rules
            # -------------------------------------

            sections.append(
                "Never change this character's personality."
            )

            sections.append(
                "Keep the speaking style consistent."
            )

            sections.append(
                "Use natural dialogue. "
                "Do not force personality traits "
                "into every sentence."
            )

            sections.append(
                "Stay completely consistent "
                "throughout the story."
            )

            sections.append("")

        return "\n".join(
            sections
        )