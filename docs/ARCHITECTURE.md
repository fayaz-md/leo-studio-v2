# 🦁 Leo Studio V2 Architecture

## Overview

Leo Studio is a modular AI-powered animation production pipeline designed to create high-quality animated episodes with consistent characters.

The architecture follows the **Single Responsibility Principle** and a **Provider Pattern**, allowing each component to evolve independently.

---

# High-Level Architecture

```
                   User
                     │
                     ▼
              leo_studio.py
                     │
                     ▼
             Story Generator
                     │
                     ▼
                story.json
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
Character      Voice Generator   Prompt Generator
 Manager             │                │
     │               ▼                ▼
     │           audio/          prompts/
     │                                │
     │                                ▼
     │                      Meta AI (Manual)
     │                                │
     ▼                                ▼
characters/                       images/
           \                      /
            \                    /
             ▼                  ▼
             Timeline Builder
                     │
                     ▼
               timeline.json
                     │
                     ▼
              Video Renderer
                     │
                     ▼
                episode.mp4
```

---

# Core Modules

## Story Engine

Responsible for:

- Story generation
- Scene generation
- Dialogue generation
- Metadata generation

Output:

```
story.json
```

---

## Character Manager

Responsible for:

- Character loading
- Character storage
- Character lookup
- Scene character detection

Output:

```
Character objects
```

---

## Voice Engine

Responsible for:

- Voice selection
- Emotion handling
- Audio generation

Output:

```
audio/
    scene_001.mp3
    scene_002.mp3
    ...
```

---

## Prompt Engine

Responsible for:

- Image prompt generation
- Character appearance injection
- Camera instructions
- Style instructions

Output:

```
prompts/
    scene_001.txt
    scene_002.txt
```

---

## Image Pipeline

Current Provider:

- Meta AI (Manual)

Future Providers:

- OpenAI Images
- Gemini Images
- ComfyUI
- Stable Diffusion

Output:

```
images/
    scene_001.png
    scene_002.png
```

---

## Timeline Engine

Responsible for:

- Scene duration
- Audio mapping
- Image mapping
- Camera effects
- Transitions

Output:

```
timeline.json
```

---

## Video Engine

Responsible for:

- Scene rendering
- Ken Burns effects
- Scene transitions
- Final MP4 generation

Output:

```
episode.mp4
```

---

# Provider Architecture

Leo Studio uses interchangeable providers.

```
StoryGenerator
      │
      ▼
StoryProvider
      │
 ┌────┴─────┐
 ▼          ▼
Gemini   Future AI
```

```
VoiceGenerator
      │
      ▼
VoiceProvider
      │
 ┌────┴─────┐
 ▼          ▼
EdgeTTS   ElevenLabs
```

```
VideoRenderer
      │
      ▼
VideoProvider
      │
 ┌────┴─────┐
 ▼          ▼
FFmpeg   Future Providers
```

---

# Design Principles

- Modular architecture
- Single Responsibility Principle
- Provider-based integrations
- Clear separation of concerns
- Future-proof extensibility
- Human-readable project outputs
- Git versioning for every milestone

---

# Current Workflow

```
Story Idea
      │
      ▼
Story Generation
      │
      ▼
Voice Generation
      │
      ▼
Prompt Generation
      │
      ▼
Meta AI Image Creation
      │
      ▼
Timeline Generation
      │
      ▼
Video Rendering
      │
      ▼
Final MP4
```

---

# Current Version

```
Leo Studio v2.3.0
```

Status:

- Foundation ✅
- Story Engine ✅
- Voice Engine ✅
- Prompt Engine ✅
- Image Pipeline ✅
- Timeline Engine ✅
- Video Engine 🚧