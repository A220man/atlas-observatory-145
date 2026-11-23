# deep_tutor/api/routers/courses.py

"""Course access with enrollment gating for learner accounts.

A learner holding the `courses` learning surface may only read course detail
and run course-scoped operations for courses they are enrolled in. Listing and
creating courses stay open to that surface; membership is checked for
course-scoped paths of the form ``/api/courses/{course_id}...``.
"""

from typing import Iterable, Optional, Tuple

_COURSES_PREFIX = "/api/courses"

# Actions on a specific course that require an enrollment check.
_ENROLLED_ACTIONS = frozenset({"", "detail", "materials", "sessions", "progress"})


def _split_course_path(path: str) -> Tuple[Optional[str], str]:
    """Return ``(course_id, action)`` for a course-scoped path, else ``(None, "")``.

    ``/api/courses``            -> (None, "")       (listing)
    ``/api/courses/new``        -> (None, "new")    (collection action)
    ``/api/courses/42``         -> ("42", "")       (detail)
    ``/api/courses/42/notes``   -> ("42", "notes")  (scoped action)
    """
    if not path.startswith("/"):
        path = "/" + path
    if not path.startswith(_COURSES_PREFIX):
        return None, ""
    rest = path[len(_COURSES_PREFIX):]
    if rest in ("", "/"):
        return None, ""
    parts = [segment for segment in rest.split("/") if segment]
    if not parts:
        return None, ""
    if parts[0] in ("new", "search"):
        return None, parts[0]
    course_id = parts[0]
    action = parts[1] if len(parts) > 1 else ""
    return course_id, action


def is_enrollment_required(path: str) -> bool:
    """True when the path targets one course and the action needs enrollment."""
    course_id, action = _split_course_path(path)
    if course_id is None:
        return False
    return action in _ENROLLED_ACTIONS


def can_access_course(course_id: str, enrolled_course_ids: Iterable[str]) -> bool:
    """Return True when the learner is enrolled in ``course_id``."""
    return course_id in set(enrolled_course_ids)


def assert_course_access(
    path: str,
    enrolled_course_ids: Iterable[str],
) -> None:
    """Raise PermissionError when an enrollment-gated path is not permitted.

    Non-enrollment paths (listing, creation, collection search) pass through
    unchanged so the ``courses`` surface keeps working for every learner.
    """
    if not is_enrollment_required(path):
        return
    course_id, _ = _split_course_path(path)
    if course_id is None:  # pragma: no cover - guarded by is_enrollment_required
        return
    if not can_access_course(course_id, enrolled_course_ids):
        raise PermissionError(
            f"Learner is not enrolled in course '{course_id}'."
        )
