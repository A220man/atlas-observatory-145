# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

learner-course-enrollment

## Roadmap

### learners-courses-access — Fix learner 403 on /api/courses

Status: done

Acceptance:
- Learner accounts with preset=learner can access /api/courses without 403; UI does not mask with empty state

Implementation: `deep_tutor/api/routers/auth.py`, `deep_tutor/multi_user/learning_access.py`

Tests: `test_api_learning_access.py`

### learner-course-enrollment — Gate learner course detail by enrollment

Status: done

Acceptance:
- Learner with courses surface can list/create/search courses
- Reading detail/materials/progress of a non-enrolled course raises PermissionError
- Collection actions are not enrollment-gated

Implementation: `deep_tutor/api/routers/courses.py`

Tests: `test_course_access.py`

