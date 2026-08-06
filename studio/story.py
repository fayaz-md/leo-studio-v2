import json

from studio.providers.gemini_provider import GeminiProvider
from studio.story_parser import StoryParser
from studio.prompt_builder import PromptBuilder

from studio.extractors.metadata_extractor import (
    MetadataExtractor,
)


class StoryGenerator:

    def __init__(self):

        self.provider = GeminiProvider()

        self.parser = StoryParser()

        self.prompt_builder = PromptBuilder()

        self.metadata_extractor = MetadataExtractor()

    def generate(self, story_idea):

        prompt = self.prompt_builder.build_story_prompt(
            story_idea=story_idea
        )

        raw_response = self.provider.generate(prompt)

        story_data = self._extract_json(raw_response)

        metadata = self.metadata_extractor.extract(
            story_data
        )

        story_data["characters"] = metadata.get(
            "characters",
            [],
        )

        story_data["locations"] = metadata.get(
            "locations",
            [],
        )

        story_data["props"] = metadata.get(
            "props",
            [],
        )
        print("\n========== STORY DATA BEFORE PARSER ==========")
        print(json.dumps(story_data, ensure_ascii=False, indent=4))
        print("=============================================\n")
        story = self.parser.parse(
            json.dumps(
                story_data,
                ensure_ascii=False,
                indent=4,
            )
        )
        return story

    def _extract_json(self, text):

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "No JSON found in AI response."
            )

        return json.loads(
            text[start:end + 1]
        )