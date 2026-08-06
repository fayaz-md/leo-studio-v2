import json

from studio.providers.gemini_provider import GeminiProvider
from studio.extractors.extraction_prompt_builder import (
    ExtractionPromptBuilder,
)


class MetadataExtractor:
    """
    Extracts structured metadata from a generated story.

    Returns:
    - characters
    - locations
    - props
    """

    def __init__(self):

        self.provider = GeminiProvider()
        self.prompt_builder = ExtractionPromptBuilder()

    def extract(self, story_json):

        if isinstance(story_json, dict):

            story_json = json.dumps(
                story_json,
                ensure_ascii=False,
                indent=4,
            )

        prompt = self.prompt_builder.build_metadata_prompt(
            story_json
        )

        response = self.provider.generate(prompt)
        
        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "No JSON returned by metadata extractor."
            )

        return json.loads(
            response[start:end + 1]
        )