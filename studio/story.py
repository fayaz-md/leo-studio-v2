from studio.providers.gemini_provider import GeminiProvider
from studio.story_parser import StoryParser
from studio.prompt_builder import PromptBuilder


class StoryGenerator:

    def __init__(self):

        self.provider = GeminiProvider()
        self.parser = StoryParser()
        self.prompt_builder = PromptBuilder()

    def generate(self, story_idea):

        prompt = self.prompt_builder.build_story_prompt(
            story_idea=story_idea
        )

        raw_response = self.provider.generate(prompt)

        story = self.parser.parse(raw_response)

        return story