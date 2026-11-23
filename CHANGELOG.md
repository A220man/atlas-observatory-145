# Changelog

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
