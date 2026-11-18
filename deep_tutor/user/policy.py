"""User policy definitions for learning surface access."""
from typing import Dict, Set

# Mapping from user preset to allowed learning surfaces.
# Keep in sync with _PATH_TO_SURFACE in deep_tutor/api/routers/auth.py.
_PRESET_ALLOWED_SURFACES: Dict[str, Set[str]] = {
    "learner": {"chat", "reading", "courses"},
    "instructor": {
        "chat", "reading", "courses", "question", "question-notebook",
        "sessions", "knowledge-bases", "mastery-paths"
    },
    # Additional presets can be added as needed.
}


def get_allowed_surfaces_for_preset(preset: str) -> Set[str]:
    """Return the set of allowed learning surfaces for the given user preset."""
    return _PRESET_ALLOWED_SURFACES.get(preset, set())
