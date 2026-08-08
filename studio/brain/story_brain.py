"""
Leo Studio Story Brain
"""


class StoryBrain:
    """
    Defines the ideal structure of a Leo Studio story.
    """

    def __init__(self):

        self.story_template = [

            {
                "scene": 1,
                "purpose": "Hook",
                "goal": "Grab attention immediately.",
            },

            {
                "scene": 2,
                "purpose": "Problem",
                "goal": "Clearly show the main challenge.",
            },

            {
                "scene": 3,
                "purpose": "Failed Attempt",
                "goal": "Show that solving the problem is not easy.",
            },

            {
                "scene": 4,
                "purpose": "Discovery",
                "goal": "Find a clever scientific or creative solution.",
            },

            {
                "scene": 5,
                "purpose": "Solution",
                "goal": "Solve the problem using teamwork and science.",
            },

            {
                "scene": 6,
                "purpose": "Celebration",
                "goal": "Celebrate the success and show happy emotions.",
            },

            {
                "scene": 7,
                "purpose": "Learning",
                "goal": "Teach one educational lesson and end with Leo's sign-off.",
            },

        ]

    def expected_purpose(
        self,
        scene_number,
    ):

        for scene in self.story_template:

            if scene["scene"] == scene_number:

                return scene

        return None

    def validate_scene_count(
        self,
        story,
    ):

        return len(story.scenes) >= 6