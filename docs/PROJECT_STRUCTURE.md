# 📁 Leo Studio Project Structure

Version: 1.0

---

# Purpose

This document defines the official folder structure of Leo Studio.

Every file and folder has a single responsibility.

Future development should follow this structure to keep the project modular, scalable, and easy to maintain.

---

# Project Structure

```text
LeoStudioV2/

├── assets/
├── docs/
├── projects/
├── studio/
├── tests/
├── .venv/

├── leo_studio.py
├── generate_voice.py
├── generate_prompts.py
├── generate_timeline.py
├── render_video.py

├── requirements.txt
├── README.md
└── .gitignore
```

---

# Root Directory

Contains application entry points.

These scripts are executed directly by the user.

Examples:

- leo_studio.py
- generate_voice.py
- generate_prompts.py
- generate_timeline.py
- render_video.py

Business logic should never be implemented here.

---

# assets/

Stores reusable production assets.

```text
assets/

├── characters/
├── locations/
├── props/
├── series/
├── knowledge/
├── music/
└── sfx/
```

Assets belong to Leo Studio, not individual projects.

---

## characters/

Contains permanent character profiles.

Future structure:

```text
characters/

registry.json

leo/

profile.json

reference.png

rabbit_mimi/

profile.json

reference.png
```

Every recurring character is stored only once.

---

## locations/

Reusable world locations.

Examples:

- Forest
- River
- School
- Village
- Space Station

---

## props/

Reusable objects.

Examples:

- Balloon
- Basket
- Rocket
- Telescope
- Treasure Chest

---

## series/

Series configuration.

Examples:

- Leo Adventures
- Leo Science Lab
- Leo History Time
- Leo Space Explorer

Each series defines:

- Main Character
- Template
- Genre
- Audience
- Rules

---

## knowledge/

Future educational knowledge base.

Examples:

- Science
- Geography
- History
- Animals

Knowledge articles are reusable across episodes.

---

## music/

Background music library.

---

## sfx/

Sound effects library.

---

# docs/

Project documentation.

Examples:

- ARCHITECTURE.md
- PROJECT_STRUCTURE.md
- ROADMAP.md
- QUALITY_GUIDELINES.md
- LEO_UNIVERSE.md
- CHANGELOG.md

Documentation should always reflect the current architecture.

---

# projects/

Generated project workspace.

Example:

```text
projects/

Leo_helps_a_lost_rabbit/

story.json

images/

audio/

timeline.json

final_video.mp4
```

Each project is self-contained.

---

# studio/

Contains all application logic.

Future structure:

```text
studio/

engines/

providers/

templates/

managers/

models/

utils/
```

---

## engines/

Core business logic.

Examples:

- Story Engine
- Character Engine
- Image Engine
- Audio Engine
- Timeline Engine
- Video Engine
- Knowledge Engine

Each engine has one responsibility.

---

## providers/

External service integrations.

Examples:

- Gemini
- Edge TTS
- FFmpeg
- Meta AI (future)
- OpenAI (future)

Providers should be replaceable.

---

## templates/

Story templates.

Examples:

- Adventure
- Science
- History
- Quiz
- Facts

Templates define how stories are generated.

---

## managers/

High-level coordination components.

Examples:

- CharacterManager
- CharacterRegistry
- ProjectManager
- VoiceManager

Managers coordinate assets and engines.

---

## models/

Shared data models.

Examples:

- Story
- Scene
- Character
- Timeline

---

## utils/

Reusable helper utilities.

Examples:

- File utilities
- JSON helpers
- Validation
- Logging

---

# tests/

Future automated tests.

Examples:

- Unit Tests
- Integration Tests
- Rendering Tests

---

# Development Rules

- Every folder has one responsibility.
- Business logic belongs inside the studio package.
- Assets must remain reusable.
- Projects must remain independent.
- Providers should be replaceable.
- New features should fit into the existing structure rather than creating new top-level folders.

---

# Future Growth

The project structure is designed to support:

- Multiple animated series
- Universal character system
- Educational content
- Reusable worlds
- AI provider replacement
- Automated publishing
- Scalable asset libraries

---

# Status

Version: 1.0

Status: Frozen

Future development should extend this structure rather than redesign it.