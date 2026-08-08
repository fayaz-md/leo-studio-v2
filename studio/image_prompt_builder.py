from studio.character_bible import CharacterBible


class ImagePromptBuilder:

    def __init__(self):

        self.character_bible = CharacterBible()
        self.character_bible.load()

    def process(self, story):

        for scene in story.scenes:

            scene.final_image_prompt = self.build(
                scene,
                story.characters,
            )

        return story

    def build(
        self,
        scene,
        characters,
    ):

        prompt = []

        # -----------------------------------------
        # Character References
        # -----------------------------------------

        for character in characters:

            bible = self.character_bible.get(
                character.id
            )

            if bible:

                prompt.append(
                    self._describe_character(
                        bible
                    )
                )

        # -----------------------------------------
        # Scene
        # -----------------------------------------

        prompt.append("")

        prompt.append(
            scene.image_prompt
        )

        # -----------------------------------------
        # Camera
        # -----------------------------------------

        if scene.camera:

            prompt.append("")

            prompt.append(
                f"Camera: {scene.camera}"
            )

        # -----------------------------------------
        # Style
        # -----------------------------------------

        prompt.append("")

        prompt.append(
            "Pixar-quality 3D animated movie."
        )

        prompt.append(
            "Ultra detailed."
        )

        prompt.append(
            "Cinematic composition."
        )

        prompt.append(
            "Soft global illumination."
        )

        prompt.append(
            "Volumetric lighting."
        )

        prompt.append(
            "High quality rendering."
        )

        prompt.append(
            "9:16 portrait composition."
        )

        return " ".join(prompt)

    def _describe_character(
        self,
        character,
    ):
        """
        Returns the canonical visual description from the
        Character Bible.

        Falls back to a minimal description for
        unknown characters.
        """

        # -----------------------------------------
        # Preferred description
        # -----------------------------------------

        visual_description = character.get(
            "visual_description",
            "",
        )

        if visual_description:

            return visual_description

        # -----------------------------------------
        # Fallback
        # -----------------------------------------

        personality = character.get(
            "personality",
            {}
        )

        traits = personality.get(
            "traits",
            []
        )

        name = character.get(
            "display_name",
            "Character",
        )

        species = character.get(
            "species",
            "character",
        )

        sentence = f"{name} is a {species}."

        if traits:

            sentence += (
                " Personality: "
                + ", ".join(traits)
                + "."
            )

        return sentence