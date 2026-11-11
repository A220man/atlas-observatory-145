# deep_tutor/api/routers/auth.py

"""Authentication routing and surface mapping for multi-user access control."""

from typing import Dict, Optional

# Mapping from API path root to learning surface name.
# Used by _learning_surface_for_path to resolve which surface a request belongs to.
# Keep in sync with allowed_surfaces in user policies (deeptutor/user/policy.py).
_PATH_TO_SURFACE: Dict[str, str] = {
    "/api/reading": "reading",
    "/api/chat": "chat",
    "/api/question": "question",
    "/api/question-notebook": "question-notebook",
    "/api/sessions": "sessions",
    "/api/knowledge-bases": "knowledge-bases",
    "/api/mastery-paths": "mastery-paths",
    "/api/courses": "courses",  # Added to support learner access to courses
}

def _learning_surface_for_path(path: str) -> str:
    """Return the learning surface for the given request path, or empty string if unknown."""

    # Normalize: strip query string, fragment, ensure leading slash.
    if not path.startswith("/"):
        path = "/" + path

    # Check exact prefix; order matters for longest match if we extend.
    for prefix, surface in _PATH_TO_SURFACE.items():
        if path == prefix or path.startswith(prefix + "/"):
            return surface
    return ""