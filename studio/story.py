from studio.providers.gemini_provider import GeminiProvider
from studio.story_parser import StoryParser
from studio.prompt_builder import PromptBuilder

class StoryGenerator:

    def __init__(self):

        self.provider = GeminiProvider()

        self.parser = StoryParser()
        self.prompt_builder = PromptBuilder()
# TODO:
# Remove this method after Story Engine V3 is fully validated.
# Prompt generation has moved to PromptBuilder.build_story_prompt().
    def build_prompt(self, story_idea):

        return f"""
You are an expert Pixar writer.

Return ONLY valid JSON.

Do NOT use markdown.

Story language: Hindi.

Create EXACTLY 8 scenes.

Main Character:
Leo

Appearance:
Cute golden lion cub.
Golden-yellow fur.
Fluffy orange mane.
Pink nose.
Big expressive eyes.
Same appearance in every scene.

Story Idea:
{story_idea}

Return JSON in this format:

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

    def generate(self, story_idea):

        prompt = self.prompt_builder.build_story_prompt(
            story_idea=story_idea
        )

        raw_response = self.provider.generate(prompt)

        story = self.parser.parse(raw_response)

        return story