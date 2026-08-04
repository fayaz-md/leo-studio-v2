from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# Studio
# --------------------------------------------------

STUDIO_NAME = "Leo Studio"
STUDIO_VERSION = "2.0.0"

# --------------------------------------------------
# Paths
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT_DIR / "assets"
PROJECTS_DIR = ROOT_DIR / "projects"

# --------------------------------------------------
# Providers
# --------------------------------------------------

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TEXT_MODEL = "gemini-3.5-flash"

STORY_PROVIDER = "gemini"
VOICE_PROVIDER = "edge"
IMAGE_PROVIDER = "chatgpt"

# --------------------------------------------------
# Story Defaults
# --------------------------------------------------

DEFAULT_SERIES = "Leo Adventures"
DEFAULT_LANGUAGE = "Hindi"
DEFAULT_DURATION = 45

# --------------------------------------------------
# Video Defaults
# --------------------------------------------------

DEFAULT_IMAGE_STYLE = "Pixar"
DEFAULT_ASPECT_RATIO = "9:16"
DEFAULT_TARGET_PLATFORM = "YouTube Shorts"