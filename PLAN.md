# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

learners-courses-access

## Roadmap

### learners-courses-access — Fix learner 403 on /api/courses

Status: done

Acceptance:
- Learner accounts with preset=learner can access /api/courses without 403; UI does not mask with empty state

Implementation: `deep_tutor/api/routers/auth.py`, `deep_tutor/multi_user/learning_access.py`

Tests: `test_api_learning_access.py`

