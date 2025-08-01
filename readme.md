# Book Catalog API

A simple RESTful service for managing a catalog of books, built with Django & Django REST Framework, containerized with Docker, and deployable to Kubernetes via Helm.

---

## Table of Contents

- [Overview](#overview)  
- [Prerequisites](#prerequisites)  
- [Local Setup](#local-setup)  
  - [Using Virtualenv](#using-virtualenv)  
  - [Using Docker Compose](#using-docker-compose)  
- [API Usage](#api-usage)  
- [Running Tests](#running-tests)  
- [Docker Image](#docker-image)  
- [CI/CD Pipelines](#cicd-pipelines)  
- [Kubernetes Deployment](#kubernetes-deployment)  
  - [Helm Chart](#helm-chart)  
  - [Raw Manifests](#raw-manifests)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

This project implements a simple book catalog API with CRUD operations:

- **Create** a new book  
- **Read** a list of books or details for a single book  
- **Update** an existing book  
- **Delete** a book  

It demonstrates:

- Django + DRF application structure  
- Automated testing with `pytest`  
- Containerization with Docker & Docker Compose  
- GitHub Actions CI for testing, image build & publish, and Kubernetes deploy  
- Kubernetes deployment via Helm chart and raw manifests  

---

## Prerequisites

- **Python** ≥ 3.13  
- **Docker** & **Docker Compose**  
- **kubectl** (configured for your cluster)  
- **Helm** ≥ 3.0  
- A container registry (we use GitHub Container Registry)  
- GitHub Actions secrets:  
  - `GITHUB_TOKEN` (automatic)  
  - `KUBE_CONFIG_DATA` (your base64-encoded kubeconfig)  

---

## Local Setup

### Using Virtualenv

```bash
git clone https://github.com/gavilugron/book-catalog.git
cd book-catalog

# create & activate venv
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# apply migrations & run server
python manage.py migrate
python manage.py runserver
```
Visit http://127.0.0.1:8000/api/books/.

---

## Using Docker Compose

```
docker-compose up --build
```

- **App** listens on `localhost:8000`
- **Postgres** runs in `db` service

Shutdown with `docker-compose down`.

---

## API Usage

Assuming service on `localhost:8000`:

- **List all books**

```
curl http://localhost:8000/api/books/
```

- **Get one book**

```
curl http://localhost:8000/api/books/1/
```

- **Create a book**

```
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Dune","author":"Frank Herbert","published_date":"1965-08-01"}'
```

- **Update a book**

```
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Dune Messiah"}'
```

- **Delete a book**

```
curl -X DELETE http://localhost:8000/api/books/1/
```

---

## Running Tests

```
# with virtualenv
pytest

# via Docker
docker-compose run --rm app pytest
```
GitHub Actions automatically runs tests on every PR and push to main.

---

## Docker Image

- Build and tag locally:

```
docker build -t ghcr.io/<your-org>/book-catalog:latest .
```

- Push to GHCR:

```
docker push ghcr.io/<your-org>/book-catalog:latest
```

---

## CI/CD Pipelines

- `.github/workflows/test.yml`
Runs migrations and `pytest` on push/PR to `main`.

- `.github/workflows/ci-build.yml`
Builds your Docker image via Buildx and pushes to GHCR.

- `.github/workflows/ci-deploy.yml`
Decodes `KUBE_CONFIG_DATA`, then runs `helm upgrade --install` to deploy the new image.

---

## Kubernetes Deployment

### Helm Chart

Chart directory: `books-catalog-chart/`

```
# deploy to default namespace
helm upgrade --install book-catalog ./books-catalog-chart \
  --namespace default \
  --set image.repository=ghcr.io/<your-org>/book-catalog \
  --set image.tag=latest
```

### Raw Manifests

Under `k8s_yamls/`:

- `application/` → Deployment, Service, Ingress, Job, Secrets

- `postgres/` → Namespace, PVC, StatefulSet, Service, ConfigMap, Secrets, etc.

Apply with:

```
kubectl apply -f k8s_yamls/postgres/
kubectl apply -f k8s_yamls/application/
```

---

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit with Conventional Commits
4. Open a Pull Request

---

## License

This project is released under the MIT License.