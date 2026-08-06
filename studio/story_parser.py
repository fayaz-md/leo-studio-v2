import json

from studio.models import (
    Story,
    Metadata,
    Settings,
    Character,
    Location,
    Prop,
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

        # -----------------------------------------
        # Characters
        # -----------------------------------------

        characters = []

        for c in data.get("characters", []):

            characters.append(
                Character(
                    id=c.get("id", ""),
                    display_name=c.get("display_name", ""),
                    species=c.get("species", ""),
                    gender=c.get("gender", ""),
                    age=c.get("age", ""),
                    role=c.get("role", ""),
                    voice_profile=c.get("voice_profile", ""),
                    personality=c.get("personality", {}),
                    appearance=c.get("appearance", {}),
                    relationships=c.get("relationships", {}),
                    catchphrase=c.get("catchphrase", ""),
                    default_emotion=c.get("default_emotion", "happy"),
                    locked=c.get("locked", False),
                )
            )

        # -----------------------------------------
        # Locations
        # -----------------------------------------

        locations = []

        for location in data.get("locations", []):

            locations.append(
                Location(
                    id=location.get("id", ""),
                    name=location.get("name", ""),
                    description=location.get(
                        "description",
                        "",
                    ),
                )
            )

        # -----------------------------------------
        # Props
        # -----------------------------------------

        props = []

        for prop in data.get("props", []):

            props.append(
                Prop(
                    id=prop.get("id", ""),
                    name=prop.get("name", ""),
                    description=prop.get(
                        "description",
                        "",
                    ),
                )
            )

        scenes = []
                # -----------------------------------------
        # Scenes
        # -----------------------------------------

        for scene in data.get("scenes", []):

            dialogues = []

            for dialogue in scene.get("dialogues", []):

                dialogues.append(
                    Dialogue(
                        speaker=dialogue.get(
                            "speaker",
                            "",
                        ),
                        emotion=dialogue.get(
                            "emotion",
                            "happy",
                        ),
                        text=dialogue.get(
                            "text",
                            "",
                        ),
                    )
                )

            scenes.append(
                Scene(
                    id=f"scene_{scene.get('number', 0):03}",
                    number=scene.get(
                        "number",
                        0,
                    ),
                    title=scene.get(
                        "title",
                        "",
                    ),
                    narration=scene.get(
                        "narration",
                        "",
                    ),
                    image_prompt=scene.get(
                        "image_prompt",
                        "",
                    ),
                    animation_prompt=scene.get(
                        "animation_prompt",
                        "",
                    ),
                    camera=scene.get(
                        "camera",
                        "",
                    ),
                    music=scene.get(
                        "music",
                        "",
                    ),
                    sfx=scene.get(
                        "sfx",
                        "",
                    ),
                    dialogues=dialogues,
                )
            )

        return Story(
            metadata=metadata,
            settings=settings,
            characters=characters,
            locations=locations,
            props=props,
            scenes=scenes,
        )