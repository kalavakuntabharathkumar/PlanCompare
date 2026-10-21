# PlanCompare API

FastAPI endpoints: `GET /health`, `GET /api/plans`, `GET /api/plans/{plan_id}`, and `POST /api/estimate`. SQLite is initialized on application startup and seeded with four sample plan options. The estimator is deterministic and covered by pytest.
