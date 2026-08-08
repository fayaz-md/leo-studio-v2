from datetime import datetime


class ProductionReport:

    def generate(
        self,
        story,
        critic_report,
    ):

        report = {

            "project": story.metadata.project_name,

            "episode": story.metadata.episode,

            "episode_title": story.metadata.episode_title,

            "generated_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "summary": {

                "scene_count": len(
                    story.scenes
                ),

                "duration": sum(
                    scene.duration
                    for scene in story.scenes
                ),

                "character_count": len(
                    story.characters
                ),

                "location_count": len(
                    story.locations
                ),

                "prop_count": len(
                    story.props
                ),

            },

            "quality": {

                "overall_score": critic_report[
                    "overall_score"
                ],

                "scene_scores": critic_report[
                    "scene_scores"
                ],

            },

            "status": {

                "story_generated": True,

                "storyboard_generated": True,

                "timeline_generated": True,

                "production_ready": True,

            }

        }

        return report