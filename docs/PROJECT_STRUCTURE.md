# 📁 Leo Studio V2 Project Structure

## Root Directory

```
LeoStudioV2/

│
├── assets/
├── docs/
├── projects/
├── studio/
├── .venv/
│
├── leo_studio.py
├── generate_voice.py
├── generate_prompts.py
├── generate_timeline.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# assets/

Stores reusable resources.

```
assets/

characters/
voices/
music/
fonts/
logos/
```

---

## characters/

One JSON file per character.

Example:

```
leo.json
rabbit.json
monkey.json
```

These files contain:

- Appearance
- Personality
- Voice profile
- Relationships
- Default emotion

---

## voices/

Voice configuration.

Future:

```
voices/

leo.json

rabbit.json
```

---

## music/

Background music library.

Future:

```
happy.mp3

sad.mp3

adventure.mp3
```

---

# docs/

Project documentation.

```
ARCHITECTURE.md

PROJECT_STRUCTURE.md

ROADMAP.md

CHANGELOG.md

DEVELOPMENT_GUIDE.md
```

---

# projects/

Each generated episode has its own folder.

Example:

```
Leo_helps_a_lost_rabbit/

story.json

timeline.json

script.md

prompts/

images/

audio/

final/
```

---

## prompts/

```
scene_001.txt

scene_002.txt
```

---

## images/

```
scene_001.png

scene_002.png
```

---

## audio/

```
scene_001.mp3

scene_002.mp3
```

---

## final/

Future rendered videos.

```
episode.mp4

thumbnail.png
```

---

# studio/

Core Leo Studio source code.

```
studio/

config.py

models.py

serializer.py

story.py

story_parser.py

character_manager.py

voice_manager.py

prompt_builder.py

timeline.py
```

---

## providers/

Provider implementations.

```
providers/

gemini_provider.py

edge_provider.py

video_provider.py
```

Future:

```
openai_provider.py

comfy_provider.py

elevenlabs_provider.py

ffmpeg_provider.py
```

---

# Design Rules

- One responsibility per module.
- Provider pattern for external services.
- Generated files are stored only inside `projects/`.
- Reusable resources belong in `assets/`.
- Documentation belongs in `docs/`.
- Core business logic belongs in `studio/`.

---

# Version

```
Leo Studio v2.3.0
```