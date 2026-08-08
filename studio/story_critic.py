class StoryCritic:

    def evaluate(self, story):

        report = {
            "overall_score": 0,
            "scene_scores": []
        }

        total_score = 0

        for scene in story.scenes:

            scene_report = self.evaluate_scene(scene)

            report["scene_scores"].append(
                scene_report
            )

            total_score += scene_report["overall"]

        if story.scenes:

            report["overall_score"] = round(
                (total_score * 20) / len(story.scenes),
                1
            )

        return report

    def evaluate_scene(self, scene):

        ratings = {}

        ratings["Hook"] = self.score_hook(scene)

        ratings["Dialogue"] = self.score_dialogue(scene)

        ratings["Emotion"] = self.score_emotion(scene)

        ratings["Curiosity"] = self.score_curiosity(scene)

        ratings["Purpose"] = self.score_purpose(scene)

        overall = round(
            sum(ratings.values()) / len(ratings)
        )

        return {

            "scene": scene.number,

            "ratings": ratings,

            "overall": overall

        }

    # -----------------------------------------

    def score_hook(self, scene):

        text = (
            scene.narration.lower()
            + " "
            + scene.title.lower()
        )

        keywords = [

            "help",

            "emergency",

            "danger",

            "boom",

            "suddenly",

            "stop",

            "warning",

            "mystery",

            "surprise",

            "oh no",

            "wait",

        ]

        score = 3

        if scene.number == 1:

            for word in keywords:

                if word in text:

                    score += 2

                    break

        return min(score, 5)

    # -----------------------------------------

    def score_dialogue(self, scene):

        if not scene.dialogues:

            return 1

        if len(scene.dialogues) == 1:

            return 3

        if len(scene.dialogues) >= 2:

            return 5

        return 2

    # -----------------------------------------

    def score_emotion(self, scene):

        text = scene.narration.lower()

        emotions = [

            "happy",

            "sad",

            "worried",

            "excited",

            "surprised",

            "scared",

            "relieved",

            "smiled",

            "laughed",

            "cried",

        ]

        for emotion in emotions:

            if emotion in text:

                return 5

        return 3

    # -----------------------------------------

    def score_curiosity(self, scene):

        text = (
            scene.narration.lower()
            + " "
            + scene.animation_prompt.lower()
        )

        words = [

            "suddenly",

            "unexpected",

            "mystery",

            "unknown",

            "wait",

            "but",

            "however",

            "then",

        ]

        for word in words:

            if word in text:

                return 5

        return 3

    # -----------------------------------------

    def score_purpose(self, scene):

        if len(scene.narration) > 40:

            return 5

        if len(scene.narration) > 20:

            return 4

        return 2