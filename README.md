# DevOps Capstone

[![CI](https://github.com/PrathmeshVishwakarma/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/PrathmeshVishwakarma/devops-capstone-project/actions/workflows/ci-build.yaml)

A RESTful **Customer Accounts** microservice built with Python and Flask. The
service exposes CRUD operations for customer accounts, persists data with
SQLAlchemy, ships with automated unit tests, and is containerized for
deployment to Kubernetes.

- Public repository: <https://github.com/PrathmeshVishwakarma/devops-capstone-project>
- CI workflow: [`.github/workflows/ci-build.yaml`](.github/workflows/ci-build.yaml)
- User stories: [`user-story.md`](user-story.md)
- Kanban plan: [`docs/kanban.md`](docs/kanban.md)
- Evidence guide: [`docs/evidence.md`](docs/evidence.md)

## Project details

| Field | Value |
| --- | --- |
| Project name | **DevOps Capstone** |
| Service | Customer Accounts microservice |
| Runtime | Python 3.9 / Flask 2.1 |
| Database | SQLite (development), PostgreSQL (production) |
| Test runner | nose |
| Linter | flake8 |
| CI | GitHub Actions |
| CD | Tekton / OpenShift Pipelines |
| Port | 8080 |

## API

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/health` | Health check |
| `GET` | `/accounts` | List all accounts |
| `POST` | `/accounts` | Create an account |
| `GET` | `/accounts/<id>` | Read one account |
| `PUT` | `/accounts/<id>` | Update an account |
| `DELETE` | `/accounts/<id>` | Delete an account |

### Account fields

| Field | Type | Required |
| --- | --- | --- |
| `id` | integer | generated |
| `name` | string | yes |
| `email` | string | yes (unique) |
| `phone_number` | string | no |
| `address` | string | no |
| `date_joined` | ISO-8601 datetime | generated |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt

FLASK_APP=service:app flask run --port 8080
```

Create the database tables once:

```bash
python -c "from service import app; from service.models import db; ctx = app.app_context(); ctx.push(); db.create_all()"
```

Example requests:

```bash
curl -s http://localhost:8080/health
curl -s -X POST http://localhost:8080/accounts \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john.doe@example.com"}'
curl -s http://localhost:8080/accounts
```

## Tests and linting

```bash
flake8 service tests
nosetests -v tests
```

The test suite covers create, list, read, update, delete, health, validation,
and model serialization.

## Continuous integration

The GitHub Actions workflow at
[`.github/workflows/ci-build.yaml`](.github/workflows/ci-build.yaml) runs on
every push and pull request to `main`:

1. **Checkout** the repository.
2. Install Python 3.9 and the project dependencies.
3. **Lint** the code with flake8.
4. **Run unit tests** with nose.

## Security

- `flask-talisman` adds security headers (`X-Frame-Options`,
  `X-Content-Type-Options`, `X-XSS-Protection`, `Referrer-Policy`).
- `flask-cors` allows browser clients to call the API and exposes
  `X-Total-Count`.

See [`service/__init__.py`](service/__init__.py) for the Talisman and CORS
configuration.

## Docker

```bash
docker build -t accounts-service:1.0 .
docker run --rm -p 8080:8080 accounts-service:1.0
```

## Kubernetes / OpenShift

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get deployment,pods,replicasets,service
```

## Repository layout

```text
.
|-- .github/workflows/ci-build.yaml  # GitHub Actions CI
|-- docs/kanban.md                   # Kanban columns, labels, estimates
|-- k8s/
|   |-- deployment.yaml              # Kubernetes deployment
|   `-- service.yaml                 # Kubernetes service
|-- service/
|   |-- __init__.py                  # app factory, Talisman, CORS
|   |-- models.py                    # Account model
|   `-- routes.py                    # REST routes
|-- tests/test_accounts.py           # unit tests
|-- Dockerfile
|-- requirements.txt
|-- setup.cfg
`-- user-story.md
```
