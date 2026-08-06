class ExtractionPromptBuilder:
    """
    Builds prompts used for extracting structured
    metadata from a generated story.

    This keeps extraction separate from story generation.
    """

    def build_metadata_prompt(self, story_json: str) -> str:

        return f"""
You are an expert information extraction AI.

You are given a story in JSON format.

Your task is NOT to rewrite the story.

Your task is ONLY to extract structured metadata.

Return ONLY valid JSON.

Do NOT return markdown.

Extract the following:

1. characters
2. locations
3. props

------------------------------------------------------
CHARACTERS
------------------------------------------------------

Include every recurring character.

Each character must contain:

- id
- display_name
- species
- gender
- age
- role

Examples

{{
    "id":"leo",
    "display_name":"Leo",
    "species":"Lion",
    "gender":"Male",
    "age":"Cub",
    "role":"Hero"
}}

------------------------------------------------------
LOCATIONS
------------------------------------------------------

Return every important location.

Example

{{
    "id":"forest",
    "name":"Forest",
    "description":"Dense forest village"
}}

------------------------------------------------------
PROPS
------------------------------------------------------

Return every important object.

Example

{{
    "id":"solar_panel",
    "name":"Solar Panel",
    "description":"Converts sunlight into electricity"
}}

------------------------------------------------------
OUTPUT

Return ONLY this structure

{{
    "characters": [],
    "locations": [],
    "props": []
}}

------------------------------------------------------
STORY JSON

{story_json}
"""