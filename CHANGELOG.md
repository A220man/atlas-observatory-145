# Changelog

## 1.3.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.2.1 — work-in-progress checkpoint

- Fix: strip query string and fragment before learning-surface resolution
  (`deep_tutor/api/routers/auth.py`) and course-id parsing
  (`deep_tutor/api/routers/courses.py`). Parameterized requests such as
  `/api/courses?page=2` now resolve correctly instead of yielding an empty
  surface (learner 403) or a polluted course id.
- Tests: `tests/test_course_access.py` regression added (full suite 10 passed).

Partial code published for continued development. Known issues: STATUS.md.

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

- Added `deep_tutor/api/routers/courses.py`: enrollment-gated course access
  (`_split_course_path`, `is_enrollment_required`, `can_access_course`,
  `assert_course_access`). Learner with the `courses` surface can list/create/search
  courses, but course-scoped reads require enrollment.
- Tests: `tests/test_course_access.py` (full suite 9 passed).

Partial code published for continued development. Known issues: STATUS.md.

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.
