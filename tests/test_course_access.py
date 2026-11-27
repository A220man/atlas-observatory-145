"""Enrollment gating for learner course access."""

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deep_tutor.api.routers.auth import _learning_surface_for_path
from deep_tutor.api.routers.courses import (
    _split_course_path,
    assert_course_access,
    can_access_course,
    is_enrollment_required,
)
from deep_tutor.multi_user.learning_access import assert_learning_surface
from deep_tutor.user.policy import get_allowed_surfaces_for_preset


def test_course_path_parsing():
    assert _split_course_path("/api/courses") == (None, "")
    assert _split_course_path("/api/courses/new") == (None, "new")
    assert _split_course_path("/api/courses/42") == ("42", "")
    assert _split_course_path("/api/courses/42/materials") == ("42", "materials")
    assert _split_course_path("/api/chat") == (None, "")


def test_enrollment_required_only_for_scoped_reads():
    assert is_enrollment_required("/api/courses") is False
    assert is_enrollment_required("/api/courses/new") is False
    assert is_enrollment_required("/api/courses/42") is True
    assert is_enrollment_required("/api/courses/42/progress") is True
    assert is_enrollment_required("/api/courses/42/notes") is False


def test_can_access_course():
    assert can_access_course("42", {"42", "7"}) is True
    assert can_access_course("99", {"42", "7"}) is False


def test_assert_course_access_denies_non_enrolled():
    with pytest.raises(PermissionError, match="not enrolled in course '99'"):
        assert_course_access("/api/courses/99", {"42"})


def test_assert_course_access_allows_enrolled_and_listing():
    # Enrolled learner passes.
    assert_course_access("/api/courses/42/materials", {"42"})
    # Listing and creation are not enrollment-gated.
    assert_course_access("/api/courses", {"42"})
    assert_course_access("/api/courses/new", set())


def test_learner_surface_reaches_courses_and_enforces_enrollment():
    allowed = get_allowed_surfaces_for_preset("learner")
    assert "courses" in allowed
    assert_learning_surface("courses", allowed)
    assert _learning_surface_for_path("/api/courses/42") == "courses"
    assert_course_access("/api/courses/42", allowed and {"42"})
    with pytest.raises(PermissionError):
        assert_course_access("/api/courses/other", allowed and {"42"})


def test_query_and_fragment_do_not_break_surface_or_enrollment():
    # Surface resolution must ignore query/fragment (regression for learner 403).
    assert _learning_surface_for_path("/api/courses?page=2") == "courses"
    assert _learning_surface_for_path("/api/courses#top") == "courses"
    assert _learning_surface_for_path("/api/courses/42?tab=notes") == "courses"

    # Course id parsing must ignore query/fragment.
    assert _split_course_path("/api/courses/42?tab=notes") == ("42", "")
    assert _split_course_path("/api/courses/42/materials#x") == ("42", "materials")

    # An enrolled learner is not wrongly denied because of a query string.
    assert_course_access("/api/courses/42?tab=notes", {"42"})
    with pytest.raises(PermissionError):
        assert_course_access("/api/courses/99?tab=notes", {"42"})
