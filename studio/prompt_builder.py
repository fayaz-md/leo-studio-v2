from studio.config import (
    DEFAULT_IMAGE_STYLE,
    DEFAULT_ASPECT_RATIO,
    DEFAULT_LANGUAGE,
    DEFAULT_DURATION,
    DEFAULT_SERIES,
)

from studio.story_schema import StorySchema


class PromptBuilder:
    """
    Central Prompt Builder for Leo Studio.

    Responsibilities
    ----------------
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

        json_contract = StorySchema.json_contract()

        return f"""
You are an award-winning Pixar writer, children's storyteller and animation director.

Return ONLY valid JSON.

Do NOT return markdown.

======================================================
LANGUAGE
======================================================

{language}

======================================================
SERIES
======================================================

{series}

======================================================
MAIN CHARACTER
======================================================

{main_character}

======================================================
TARGET AUDIENCE
======================================================

Children aged 4–10 years.

======================================================
TARGET DURATION
======================================================

Approximately {target_duration}–60 seconds.

======================================================
STORY REQUIREMENTS
======================================================

• Begin with a strong hook.
• Never begin with "One day..."
• Every scene must move the story forward.
• Prefer dialogue over narration.
• Keep narration concise.
• Show emotions through actions.
• Include a meaningful educational takeaway.
• End with Leo's official sign-off.
• Create 6–8 scenes.

======================================================
CHARACTER RULES
======================================================

Leo is ALWAYS:

• A small lion cub
• Golden-yellow fur
• Fluffy orange mane
• Pink nose
• Large expressive brown eyes

Leo is NEVER:

• Human
• Boy
• Child
• Teenager

Never change Leo's species.

Never invent clothes for Leo.

Always use "Leo" instead of:
- the lion
- the cub
- the animal

Recurring characters must always keep:
- the same name
- the same species
- the same personality
- the same appearance
- the same role

======================================================
MANDATORY JSON REQUIREMENTS
======================================================

Your response MUST contain ALL of these arrays.

They are REQUIRED.

Never leave them empty.

If any array is empty, regenerate your answer before responding.

------------------------------------------------------
characters
------------------------------------------------------

Include every important recurring character.

Each character MUST contain:

- id
- display_name
- species
- gender
- age
- role

Example

{{
"id":"leo",
"display_name":"Leo",
"species":"Lion",
"gender":"Male",
"age":"Cub",
"role":"Hero"
}}

{{
"id":"meera",
"display_name":"Meera",
"species":"Human",
"gender":"Female",
"age":"Child",
"role":"Friend"
}}

{{
"id":"robbie",
"display_name":"Robbie",
"species":"Robot",
"gender":"Unknown",
"age":"Unknown",
"role":"Helper"
}}

------------------------------------------------------
locations
------------------------------------------------------

Return every important location.

Example

[
{{
"id":"forest",
"name":"Forest"
}}
]

------------------------------------------------------
props
------------------------------------------------------

Return every important object.

Example

[
{{
"id":"solar_panel",
"name":"Solar Panel"
}}
]

Never return:

"characters": []

Never return:

"locations": []

Never return:

"props": []
======================================================
IMAGE PROMPT RULES
======================================================

The image_prompt should describe ONLY:

• Character actions
• Character expressions
• Environment
• Lighting
• Camera angle
• Composition

Never describe recurring character appearance.

Leo Studio automatically injects appearance.

======================================================
VISUAL QUALITY
======================================================

Every image should include:

• Cinematic composition
• Pixar-quality 3D animation
• Dynamic poses
• Beautiful lighting
• Family-friendly atmosphere
• Rich colors

======================================================
STORY IDEA
======================================================

{story_idea}

======================================================
OUTPUT FORMAT
======================================================

Return ONLY valid JSON.

The JSON is INVALID if:

- characters is empty
- locations is empty
- props is empty

If any of these arrays would be empty,
generate the story again before responding.

Use EXACTLY this JSON structure.

Do not omit any top-level fields.

Do not leave required arrays empty.

{json_contract}
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

            species = getattr(
                character,
                "species",
                "",
            )

            if species:
                description_parts.append(species)

            appearance = getattr(
                character,
                "appearance",
                {},
            )

            if appearance:

                description_parts.extend(
                    value
                    for value in appearance.values()
                    if value
                )

            description = ", ".join(description_parts)

            if description:
                prompt_parts.append(description)

        prompt_parts.append(
            scene.image_prompt
        )

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