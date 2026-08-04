import json

from studio.models import (
    Story,
    Metadata,
    Settings,
    Character,
    Scene,
    Dialogue,
)

from studio.config import (
    STUDIO_NAME,
    STUDIO_VERSION,
    DEFAULT_SERIES,
    DEFAULT_LANGUAGE,
    DEFAULT_DURATION,
    DEFAULT_IMAGE_STYLE,
    DEFAULT_ASPECT_RATIO,
    DEFAULT_TARGET_PLATFORM,
    STORY_PROVIDER,
    VOICE_PROVIDER,
    IMAGE_PROVIDER,
)


class StoryParser:

    def parse(self, text):

        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON found in AI response.")

        data = json.loads(text[start:end + 1])

        metadata = Metadata(
            project_name=data["title"],
            series=DEFAULT_SERIES,
            episode=1,
            episode_title=data["title"],
            language=DEFAULT_LANGUAGE,
            duration=DEFAULT_DURATION,
            created_at="",
            generator=STUDIO_NAME,
            version=STUDIO_VERSION,
        )

        settings = Settings(
            story_provider=STORY_PROVIDER,
            voice_provider=VOICE_PROVIDER,
            image_provider=IMAGE_PROVIDER,
            image_style=DEFAULT_IMAGE_STYLE,
            aspect_ratio=DEFAULT_ASPECT_RATIO,
            target_platform=DEFAULT_TARGET_PLATFORM,
        )

        characters = []

        scenes = []

        for scene in data["scenes"]:

            dialogues = []

            for d in scene.get("dialogues", []):

                dialogues.append(
                    Dialogue(
                        speaker=d["speaker"],
                        emotion=d.get("emotion", "happy"),
                        text=d["text"],
                    )
                )

            scenes.append(
                Scene(
                    id=f"scene_{scene['number']:03}",
                    number=scene["number"],
                    title=scene["title"],
                    narration=scene["narration"],
                    image_prompt=scene["image_prompt"],
                    animation_prompt=scene.get(
                        "animation_prompt",
                        ""
                    ),
                    camera=scene.get(
                        "camera",
                        ""
                    ),
                    music=scene.get(
                        "music",
                        ""
                    ),
                    sfx=scene.get(
                        "sfx",
                        ""
                    ),
                    dialogues=dialogues,
                )
            )

        return Story(
            metadata=metadata,
            settings=settings,
            characters=characters,
            scenes=scenes,
        )