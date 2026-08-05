# 👨‍💻 Development Guide

## Philosophy

Leo Studio is built as a modular animation production platform.

Every module should have a single responsibility and should be easy to replace without affecting the rest of the system.

---

# Development Rules

## 1. One File at a Time

Only one file should be developed or modified at a time.

Every file must be tested before moving to the next.

---

## 2. Single Responsibility Principle

Every module has one job.

Examples:

- Story Generator → Generate stories
- Voice Generator → Generate audio
- Prompt Builder → Build prompts
- Timeline Builder → Create timelines
- Video Renderer → Render videos

---

## 3. Provider Pattern

External services must always be wrapped in providers.

Examples:

- Story Provider
- Voice Provider
- Video Provider
- Future Image Provider

Business logic should never depend directly on third-party APIs.

---

## 4. Git Workflow

Every milestone should follow:

1. Implement
2. Test
3. Commit
4. Push

Suggested commit format:

vX.Y.Z - Description

Example:

v2.3.0 - Asset Pipeline Complete

---

## 5. Documentation First

Major architectural changes should be documented before implementation.

Documentation is considered part of the project.

---

## 6. Project Organization

Generated assets belong only inside the project folder.

Reusable resources belong inside assets/.

Documentation belongs inside docs/.

Business logic belongs inside studio/.

---

## 7. Future Compatibility

New features should extend the architecture instead of replacing it.

Backward compatibility should be maintained whenever possible.

---

# Coding Style

- Clear function names
- Small focused classes
- Minimal duplication
- Readable code over clever code
- Consistent formatting

---

# Project Vision

Leo Studio aims to become a complete AI-powered animation production studio capable of generating professional-quality animated episodes with minimal manual effort while maintaining consistent characters and modular architecture.