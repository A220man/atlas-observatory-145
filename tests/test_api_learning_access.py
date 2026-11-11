"""Test learning surface mapping and access control for learner accounts."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deep_tutor.api.routers.auth import _learning_surface_for_path
from deep_tutor.multi_user.learning_access import assert_learning_surface


def test_learning_surface_mapping():
    """Verify that /api/courses maps to 'courses' surface."""
    assert _learning_surface_for_path("/api/courses") == "courses"
    # Other mappings remain unchanged
    assert _learning_surface_for_path("/api/reading") == "reading"
    assert _learning_surface_for_path("/api/chat") == "chat"
    # Subpaths should map to parent surface (e.g., /api/courses/1 -> "courses")
    assert _learning_surface_for_path("/api/courses/1") == "courses"


def test_assert_learning_surface_allowed():
    """Assert that allowed surfaces pass."""
    allowed = {"courses", "reading", "chat"}
    # Should not raise
    assert_learning_surface("courses", allowed)
    assert_learning_surface("reading", allowed)


def test_assert_learning_surface_denied():
    """Assert that disallowed surfaces raise PermissionError."""
    import pytest
    allowed = {"reading", "chat"}
    with pytest.raises(PermissionError) as exc_info:
        assert_learning_surface("courses", allowed)
    assert "Learning surface 'courses' is not allowed" in str(exc_info.value)