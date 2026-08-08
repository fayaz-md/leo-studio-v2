import json

from studio.providers.gemini_provider import GeminiProvider
from studio.story_parser import StoryParser
from studio.prompt_builder import PromptBuilder
from studio.character_bible import CharacterBible
from studio.prompt_pipeline import PromptPipeline
from studio.story_critic import StoryCritic
from studio.brain.story_brain import StoryBrain
from studio.core.logger import Logger
from studio.core.exceptions import StoryParsingError
from studio.pipelines.dialogue_pipeline import DialoguePipeline
from studio.pipelines.emotion_pipeline import EmotionPipeline

from studio.storyboard.storyboard_generator import (
    StoryboardGenerator,
)

from studio.storyboard.storyboard_writer import (
    StoryboardWriter,
)

from studio.timeline.timeline_generator import (
    TimelineGenerator,
)

from studio.timeline.timeline_writer import (
    TimelineWriter,
)

from studio.production.production_report import (
    ProductionReport,
)

from studio.production.production_writer import (
    ProductionWriter,
)

from studio.director.director_pipeline import (
    DirectorPipeline,
)

from studio.extractors.metadata_extractor import (
    MetadataExtractor,
)


class StoryGenerator:

    def __init__(self):

        self.provider = GeminiProvider()

        self.parser = StoryParser()

        self.prompt_builder = PromptBuilder()

        self.metadata_extractor = MetadataExtractor()

        self.character_bible = CharacterBible()
        self.character_bible.load()

        self.prompt_pipeline = PromptPipeline()
        self.dialogue_pipeline = DialoguePipeline()
        self.director_pipeline = DirectorPipeline()
        self.emotion_pipeline = EmotionPipeline()
        self.story_critic = StoryCritic()
        self.story_brain = StoryBrain()
        self.storyboard_generator = (
           StoryboardGenerator()
        )

        self.storyboard_writer = (
            StoryboardWriter()
        )

        self.timeline_generator = (
           TimelineGenerator()
        )

        self.timeline_writer = (
            TimelineWriter()
        )

        self.production_report = (
            ProductionReport()
        )

        self.production_writer = (
            ProductionWriter()
        )       

    def generate(
        self,
        story_idea,
    ):

        # -------------------------------------------------
        # Build Prompt
        # -------------------------------------------------

        prompt = self.prompt_builder.build_story_prompt(
            story_idea=story_idea
        )

        # -------------------------------------------------
        # Generate Story
        # -------------------------------------------------

        raw_response = self.provider.generate(
            prompt
        )

        # -------------------------------------------------
        # Extract JSON
        # -------------------------------------------------

        story_data = self._extract_json(
            raw_response
        )

        # -------------------------------------------------
        # Extract Metadata
        # -------------------------------------------------

        metadata = self.metadata_extractor.extract(
            story_data
        )

        characters = []

        for character in metadata.get(
            "characters",
            [],
        ):

            enriched = self.character_bible.enrich(
                character
            )

            characters.append(
                enriched
            )

        story_data["characters"] = characters

        story_data["locations"] = metadata.get(
            "locations",
            [],
        )

        story_data["props"] = metadata.get(
            "props",
            [],
        )

        # -------------------------------------------------
        # Debug JSON
        # -------------------------------------------------

        print("\n========== STORY JSON ==========\n")

        print(
            json.dumps(
                story_data,
                indent=4,
                ensure_ascii=False,
            )
        )

        print("\n===============================\n")

        # -------------------------------------------------
        # Parse Story
        # -------------------------------------------------

        story = self.parser.parse(

            json.dumps(

                story_data,

                indent=4,

                ensure_ascii=False,

            )

        )
        if not self.story_brain.validate_scene_count(
            story
        ):
            Logger.warning(
               "Story contains fewer than 6 scenes."
            )

        # -------------------------------------------------
        # Prompt Pipeline
        # -------------------------------------------------

        story = self.prompt_pipeline.process(
            story
        )

        story = self.dialogue_pipeline.process(
           story
        )

        story = self.emotion_pipeline.process(
           story
        )
        # -------------------------------------------------
        # Director Pipeline
        # -------------------------------------------------

        story = self.director_pipeline.process(
            story
        )

        # -------------------------------------------------
        # Story Critic
        # -------------------------------------------------

        report = self.story_critic.evaluate(
            story
        )

        self.print_story_report(
            report
        )

# -------------------------------------------------
# Storyboard
# -------------------------------------------------

        storyboard = (
            self.storyboard_generator.generate(
                story
            )
        )

        self.storyboard_writer.save(

            storyboard,

            "storyboard.json",

        )
        # -------------------------------------------------
# Timeline
# -------------------------------------------------

        timeline = (
            self.timeline_generator.generate(
                story
            )
        )

        self.timeline_writer.save(

            timeline,

            "timeline.json",
        )

        # -------------------------------------------------
        # Production Report
        # -------------------------------------------------

        production_report = (
            self.production_report.generate(
                story,
                report,
            )
        )

        self.production_writer.save(
            production_report,
            "production_report.json",
        )
        return story

    # =================================================
    # Story Report
    # =================================================

    def print_story_report(
        self,
        report,
    ):

        print(
            "\n========== STORY QUALITY REPORT ==========\n"
        )

        print(
            f"Overall Score : {report['overall_score']}/100\n"
        )

        for scene in report[
            "scene_scores"
        ]:

            print(
                f"Scene {scene['scene']}"
            )

            for name, score in scene[
                "ratings"
            ].items():

                stars = (
                    "★" * score
                    + "☆" * (5 - score)
                )

                print(
                    f"{name:<12}: {stars}"
                )

            print(
                f"Overall     : {scene['overall'] * 20}/100"
            )

            print(
                "-" * 40
            )

        print(
            "\n==========================================\n"
        )

    # =================================================
    # Extract JSON
    # =================================================

    def _extract_json(
        self,
        text,
    ):

        start = text.find("{")

        end = text.rfind("}")

        if start == -1 or end == -1:

            raise StoryParsingError(
               "No JSON found in AI response."
            )

        return json.loads(
            text[
                start : end + 1
            ]
        )