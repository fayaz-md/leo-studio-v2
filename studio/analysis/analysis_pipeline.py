from studio.analysis.report import StoryAnalysis

from studio.analysis.hook_analyzer import HookAnalyzer


class AnalysisPipeline:
    """
    Runs all story analyzers and returns
    a single StoryAnalysis report.
    """

    def __init__(self):

        self.analyzers = [

            HookAnalyzer(),

            # DialogueAnalyzer(),
            # EmotionAnalyzer(),
            # CharacterAnalyzer(),
            # VisualAnalyzer(),
            # EducationAnalyzer(),
            # RetentionAnalyzer(),
            # YouTubeAnalyzer(),

        ]

    def analyze(
        self,
        story,
    ):

        report = StoryAnalysis()

        for analyzer in self.analyzers:

            report = analyzer.analyze(
                story,
                report,
            )

        self.calculate_overall_score(
            report
        )

        return report

    def calculate_overall_score(
        self,
        report,
    ):

        scores = [

            report.hook_score,

            report.dialogue_score,

            report.emotion_score,

            report.visual_score,

            report.education_score,

            report.retention_score,

            report.youtube_score,

            report.character_score,

            report.scene_flow_score,

        ]

        valid_scores = [

            score

            for score in scores

            if score > 0

        ]

        if valid_scores:

            report.overall_score = int(
                sum(valid_scores)
                / len(valid_scores)
            )

        else:

            report.overall_score = 0