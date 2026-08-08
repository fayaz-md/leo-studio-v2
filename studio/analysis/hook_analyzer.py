from studio.analysis.report import (
    SceneAnalysis,
)


class HookAnalyzer:
    """
    Evaluates the opening hook of Scene 1.
    """

    STRONG_WORDS = [

        "help",

        "emergency",

        "danger",

        "run",

        "quick",

        "save",

        "stop",

        "look",

        "boom",

        "watch",

        "warning",

        "trapped",

        "fire",

        "monster",

        "fall",

        "don't",

        "hurry",

        "alarm",

        "rescue",

        "wait",
    ]

    def analyze(
        self,
        story,
        report,
    ):

        if not story.scenes:
            return report

        scene = story.scenes[0]

        score = 0

        text = (
            scene.narration
            + " "
            + " ".join(
                d.text
                for d in scene.dialogues
            )
        ).lower()

        for word in self.STRONG_WORDS:

            if word in text:

                score += 1

        score = min(score, 5)

        analysis = SceneAnalysis(
            scene_number=1
        )

        analysis.hook_score = score

        if score >= 5:

            analysis.comments.append(
                "Excellent opening hook."
            )

        elif score >= 3:

            analysis.comments.append(
                "Good opening. More curiosity could improve it."
            )

        else:

            analysis.comments.append(
                "Weak opening. Needs immediate excitement."
            )

        report.hook_score = score * 20

        report.scenes.append(
            analysis
        )

        return report