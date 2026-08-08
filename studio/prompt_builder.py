from studio.config import (
    DEFAULT_IMAGE_STYLE,
    DEFAULT_ASPECT_RATIO,
    DEFAULT_LANGUAGE,
    DEFAULT_DURATION,
    DEFAULT_SERIES,
)

from studio.story_schema import StorySchema

from studio.prompt.character_prompt_builder import (
    CharacterPromptBuilder,
)

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
        self.character_prompt_builder = (
            CharacterPromptBuilder()
        )
    # ======================================================
    # STORY PROMPT
    # ======================================================

    def build_story_prompt(
        self,
        story_idea,
        characters=None,
        main_character="Leo",
        series=DEFAULT_SERIES,
        language=DEFAULT_LANGUAGE,
        target_duration=DEFAULT_DURATION,
    ):

        json_contract = StorySchema.json_contract()
        character_rules = (
            self.character_prompt_builder.build(
                characters or []
            )
        )
        print("\n========== CHARACTER RULES ==========\n")

        print(character_rules)

        print("\n=====================================\n")
        return f"""
You are an award-winning Pixar writer, children's storyteller and animation director.

Return ONLY valid JSON.

Do NOT return markdown.

Language: {language}

Series: {series}

Main Character: {main_character}

Target Audience:
Children aged 4–10 years.

======================================================
YOUTUBE SHORTS HOOK (MANDATORY)
======================================================

The FIRST scene is the most important.

The first 3 seconds MUST immediately grab attention.

The opening scene MUST begin with one of these:

• A surprising discovery
• A funny accident that immediately causes a problem.
• A dangerous situation
• A mystery
• A countdown
• An exciting challenge
• Someone calling Leo for help
• Robbie detecting an emergency
• Professor Owl giving an urgent warning

The audience should immediately wonder:

"What happens next?"

The first scene MUST end with an unanswered question, danger, surprise, or discovery.

Do NOT resolve the problem in the first scene.

The first scene should create curiosity that makes the audience want to continue watching.

Never begin with:

- Leo was walking...
- One day...
- Leo and Meera were...
- There was...

Every story MUST start in the middle of the action.

Examples:

GOOD:

"Leo! Don't drink that!" shouted Meera as Robbie's scanner suddenly flashed RED.

GOOD:

A loud BOOM echoed through the forest. Leo looked up in surprise.

GOOD:

"Emergency! Emergency!" Robbie announced as the river suddenly turned black.

BAD:

Leo and Meera went to the river.

BAD:

One day Leo was walking.

BAD:

Leo wanted to help.

The first scene should make viewers stop scrolling immediately.

The hook must happen BEFORE any explanation.

Do not explain the situation first.

Show the exciting moment first.

Explain it later.

The first spoken dialogue should occur within the first scene.

Avoid long narration before characters speak.

Children connect with conversations more than narration.

Target Duration:
Approximately {target_duration}–60 seconds.

YOUTUBE SHORTS STORY RULES

======================================================
SCENE PURPOSE RULES
======================================================

Every scene must have ONE clear purpose.

A scene may ONLY have one primary purpose.

Choose one:

• Hook
• Introduce the problem
• Make the problem worse
• Funny moment
• Discovery
• New idea
• Build suspense
• Teamwork
• Success
• Celebration
• Educational lesson
• Emotional moment

Never create filler scenes.

Every scene must either:

• Increase curiosity
OR
• Increase emotion
OR
• Increase tension
OR
• Move the story forward

If a scene does not have a clear purpose,
rewrite it.

• Begin with a strong hook.
• Never begin with "One day..."
• Every scene must move the story forward.
• Prefer dialogue over narration.
• Keep narration concise.
• Show emotions through actions.
• Include one meaningful educational takeaway.
• End with Leo's official sign-off.
• Create 6–8 scenes.

======================================================
CURIOSITY RULE
======================================================

Every scene should end with a reason to watch the next scene.

Examples:

Leo suddenly hears a strange sound...

Robbie's scanner flashes red...

Professor Owl quietly says,
"Wait... something is wrong."

Meera gasps in surprise.

The machine suddenly stops working.

Do not completely resolve the story until the final scene.

======================================================
EMOTION RULES
======================================================

Every scene must contain at least one visible emotion.

Examples:

Happy

Surprised

Curious

Excited

Worried

Relieved

Proud

Do not let multiple scenes have the same emotion unless necessary.

Emotions should naturally progress throughout the story.

======================================================
STORY STRUCTURE (MANDATORY)
======================================================

Every story MUST follow this structure.

Scene 1
HOOK

Immediately grab attention.
Do not explain everything.
Create curiosity.

Scene 2
PROBLEM

Show what is wrong.
Explain why it matters.

Scene 3
FAILED ATTEMPT

The first solution should NOT work.

Create suspense.

Scene 4
DISCOVERY

Leo, Meera or Robbie discovers a better idea.

Scene 5
SUCCESS

The problem is solved through teamwork,
kindness or science.

Scene 6
CELEBRATION

Show happy reactions.

End with:

• Educational takeaway

• Leo's official sign-off

Do NOT skip any stage.

{character_rules}

Dialogue should reveal personality.

======================================================
DIALOGUE PERFORMANCE
======================================================

Every dialogue MUST include the following fields.

speaker

text

emotion

action

expression

pose

gesture

voice_style

speaking_speed

camera_focus

pause_after

Example

{{
    "speaker":"Leo",

    "text":"I have an amazing idea!",

    "emotion":"excited",

    "action":"points toward the river",

    "expression":"big smile",

    "pose":"standing proudly",

    "gesture":"raises one paw",

    "voice_style":"energetic",

    "speaking_speed":"fast",

    "camera_focus":"close_up",

    "pause_after":0.5
}}

Rules

The action should describe what the character is doing.

The expression should describe the face.

The pose should describe the body posture.

The gesture should describe the movement.

The voice_style should match the emotion.

camera_focus should suggest the best shot.

pause_after should usually be between

0.2

and

1.0

seconds.

Avoid narration replacing dialogue.

Children enjoy conversations more than long narration.

------------------------------------------------------
LEO RULES
-----------------------------------------------------
Leo is ALWAYS the recurring hero of Leo Adventures.

Never change:

• Leo's name
• Leo's personality
• Leo's role

Leo Studio automatically injects Leo's visual appearance using the Character Bible.

Do NOT describe Leo's physical appearance.

RECURRING CHARACTERS

Recurring characters are canonical.

Never rename them.

Never redesign them.

Never change their personality.

Never change their role.

Only describe their actions and emotions.

Leo Studio manages their appearance using the Character Bible.

--------------------------------------------------
CHARACTERS
--------------------------------------------------

Return every important recurring character.

Each character MUST contain:

- id
- display_name
- species
- gender
- age
- role

Example:

{{
"id":"leo",
"display_name":"Leo",
"species":"Lion",
"gender":"Male",
"age":"Child",
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

--------------------------------------------------
LOCATIONS
--------------------------------------------------

Return every important location.

Example

[
{{
"id":"forest",
"name":"Forest"
}}
]

--------------------------------------------------
PROPS
--------------------------------------------------

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

--------------------------------------------------
IMAGE PROMPT RULES
--------------------------------------------------

The image_prompt should describe ONLY:

• Character actions
• Character emotions
• Environment
• Background
• Props
• Camera shot
• Camera angle
• Lighting
• Composition

Always refer to recurring characters ONLY by name.

Example:

Correct:

"Leo carefully examines the muddy river while Meera points toward the dirty water and Robbie scans the water."

Incorrect:

"A small golden lion cub examines the muddy river..."

Never describe the appearance of recurring characters.

Never mention:

• Fur color
• Mane
• Hair
• Eye color
• Nose color
• Clothes
• Height
• Species
• Age
• Accessories

Leo Studio automatically injects the complete visual appearance using the Character Bible.

Only describe what the characters are DOING.

Every image should include:

• Cinematic composition
• Pixar-quality 3D animation
• Dynamic poses
• Beautiful lighting
• Family-friendly atmosphere
• Rich colors

Every image should NEVER include:

• Character appearance
• Character clothing
• Character hairstyle
• Character colors
• Character accessories
• Text
• Watermarks
• Logos

For every scene:

The image_prompt should read like movie direction.

Good example:

"Leo carefully connects the solar panel while Meera holds the wires and Robbie projects a holographic blueprint. Warm morning sunlight filters through the forest canopy. Eye-level cinematic medium shot."

Bad example:

"A small golden lion cub with fluffy orange mane..."

--------------------------------------------------
STORY IDEA
--------------------------------------------------

{story_idea}

--------------------------------------------------
OUTPUT RULES
--------------------------------------------------

Return ONLY valid JSON.

The JSON is INVALID if:

- characters is empty
- locations is empty
- props is empty

If any required array would be empty,
regenerate the story before responding.

Use EXACTLY this JSON structure.

Do not omit any top-level fields.

Do not leave required arrays empty.

======================================================
QUALITY CHECK
======================================================

Before returning the JSON,
verify that ALL of these are true.

✓ Scene 1 has a strong hook.

✓ Every scene has a purpose.

✓ Every scene contains dialogue.

✓ Every scene creates curiosity.

✓ Every scene advances the story.

✓ Characters stay consistent.

✓ Story has an educational ending.

If any answer is NO,
rewrite the story before returning JSON.

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