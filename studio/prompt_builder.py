from studio.config import (
    DEFAULT_IMAGE_STYLE,
    DEFAULT_ASPECT_RATIO,
    DEFAULT_LANGUAGE,
    DEFAULT_DURATION,
    DEFAULT_SERIES,
)


class PromptBuilder:
    """
    Central Prompt Builder for Leo Studio.

    Responsibilities:
    - Story Prompt Generation
    - Image Prompt Generation
    - Character Prompt Generation (Future)
    - Educational Prompt Generation (Future)
    """

    def __init__(self):

        self.image_quality_prompt = (
            "cinematic lighting, "
            "Pixar-quality 3D animation, "
            "highly detailed, "
            "masterpiece quality, "
            "family friendly, "
            "vibrant colors, "
            "expressive emotions"
        )

    # ======================================================
    # STORY PROMPT
    # ======================================================

    def build_story_prompt(
        self,
        story_idea,
        main_character="Leo",
        series=DEFAULT_SERIES,
        language=DEFAULT_LANGUAGE,
        target_duration=DEFAULT_DURATION,
    ):

        return f"""
You are an award-winning Pixar writer and children's storyteller.

Return ONLY valid JSON.

Do NOT return markdown.

Language:
{language}

Series:
{series}

Main Character:
{main_character}

Target Audience:
Children aged 4–10 years.

Target Duration:
Approximately {target_duration}–60 seconds.

======================================================
STORY RULES
======================================================

• Begin with a powerful hook in the first scene.
• Never begin with "One day..."
• Build curiosity immediately.
• Every scene must move the story forward.
• Prefer character dialogue over long narration.
• Show emotions through actions.
• Finish with a satisfying ending.
• Include a positive moral or educational takeaway.
• End with the official Leo series sign-off.
• Generate 6–8 scenes depending on the story.

======================================================
CHARACTER RULES
======================================================

Leo is the hero of Leo Adventures.

Leo is ALWAYS an animated lion cub.

Leo's permanent appearance:

• Species: Lion Cub
• Fur: Golden-yellow
• Mane: Small fluffy orange mane
• Eyes: Large expressive brown eyes
• Nose: Pink
• Tail: Lion tail with orange tuft

These characteristics NEVER change.

Leo is NEVER:

- Human
- Boy
- Child
- Kid
- Teenager

Never change Leo's species.

Never invent clothes for Leo.

Always refer to Leo by his name.

GOOD:

Leo smiles happily.

Leo points towards the rainwater tank.

Leo jumps with excitement.

BAD:

The cub smiles...

The lion smiles...

The animal smiles...

The boy smiles...

======================================================
IMAGE PROMPT RULES
======================================================

The image_prompt should describe ONLY:

• Character actions
• Character emotions
• Character interaction
• Environment
• Lighting
• Camera
• Composition

Do NOT describe recurring character appearance.

Leo Studio automatically injects character appearance.

======================================================
VISUAL QUALITY
======================================================

Every image should include:

• Cinematic composition
• Camera angle
• Lighting
• Character expressions
• Dynamic poses
• Pixar-quality animation style

======================================================
STORY IDEA
======================================================

{story_idea}

======================================================
OUTPUT FORMAT
======================================================

Return ONLY valid JSON using EXACTLY this structure:

{{
    "title":"",
    "summary":"",
    "youtube_title":"",
    "description":"",
    "tags":[""],
    "ending_message":"",
    "scenes":[
        {{
            "number":1,
            "title":"",
            "narration":"",
            "image_prompt":"",
            "animation_prompt":"",
            "camera":"",
            "music":"",
            "sfx":"",
            "dialogues":[
                {{
                    "speaker":"",
                    "emotion":"happy",
                    "text":""
                }}
            ]
        }}
    ]
}}
"""

    # ======================================================
    # IMAGE PROMPT
    # ======================================================

    def build_image_prompt(
        self,
        scene,
        characters,
    ):

        prompt_parts = []

        prompt_parts.append(
            f"{DEFAULT_IMAGE_STYLE} style"
        )

        prompt_parts.append(
            f"Vertical {DEFAULT_ASPECT_RATIO}"
        )

        for character in characters:

            description_parts = []

            # Character species
            species = getattr(character, "species", None)

            if species:
                description_parts.append(species)

            # Character appearance
            appearance = character.appearance

            description_parts.extend(
                value
                for value in appearance.values()
                if value
            )

            description = ", ".join(description_parts)

            if description:
                prompt_parts.append(description)

        prompt_parts.append(scene.image_prompt)

        if scene.camera:
            prompt_parts.append(
                f"Camera: {scene.camera}"
            )

        prompt_parts.append(
            self.image_quality_prompt
        )

        return ", ".join(prompt_parts)

    # ======================================================
    # BACKWARD COMPATIBILITY
    # ======================================================

    def build(
        self,
        scene,
        characters,
    ):
        """
        Backward compatibility.

        Existing code still calls build().
        """

        return self.build_image_prompt(
            scene,
            characters,
        )

    # ======================================================
    # FUTURE
    # ======================================================

    def build_character_prompt(self):
        raise NotImplementedError

    def build_voice_prompt(self):
        raise NotImplementedError

    def build_educational_prompt(self):
        raise NotImplementedError