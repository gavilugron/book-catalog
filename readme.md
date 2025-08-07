# Book Catalog API

A comprehensive RESTful service for managing a catalog of books, built with Django \& Django REST Framework. The project demonstrates modern DevOps practices with containerization, multiple deployment strategies, and GitOps workflows using ArgoCD.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
    - [Using Virtual Environment](#using-virtual-environment)
    - [Using Docker Compose](#using-docker-compose)
- [API Usage](#api-usage)
- [Testing](#testing)
- [Docker](#docker)
- [CI/CD Pipelines](#cicd-pipelines)
- [Kubernetes Deployment](#kubernetes-deployment)
    - [Helm Chart Deployment](#helm-chart-deployment)
    - [Raw Kubernetes Manifests](#raw-kubernetes-manifests)
    - [ArgoCD GitOps](#argocd-gitops)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


## Overview

This project implements a book catalog API with full CRUD operations and demonstrates enterprise-grade DevOps practices:

**Core Features:**

- **Create** new books with title, author, ISBN, and publication date
- **Read** books with list and detail views
- **Update** existing book information
- **Delete** books from the catalog
- **Health check** endpoint for monitoring

**DevOps \& Infrastructure Features:**

- Django + Django REST Framework application architecture
- Comprehensive test suite with pytest
- Docker containerization with multi-stage builds
- PostgreSQL database with persistent storage
- Multiple Kubernetes deployment strategies
- Helm charts for package management
- ArgoCD for GitOps continuous deployment
- GitHub Container Registry integration
- Automated CI/CD pipelines


## Architecture

The application follows a cloud-native architecture with:

- **Application Layer**: Django REST Framework API
- **Database Layer**: PostgreSQL with persistent volumes
- **Container Layer**: Docker with optimized images
- **Orchestration Layer**: Kubernetes with Helm charts
- **GitOps Layer**: ArgoCD for automated deployments
- **CI/CD Layer**: GitHub Actions workflows


## Prerequisites

**Development Requirements:**

- Python ≥ 3.13
- Docker \& Docker Compose
- Git

**Deployment Requirements:**

- kubectl (configured for your Kubernetes cluster)
- Helm ≥ 3.0
- ArgoCD (optional, for GitOps deployment)

**CI/CD Requirements:**

- GitHub Container Registry access
- GitHub Actions secrets:
    - `GITHUB_TOKEN` (automatically provided)
    - `KUBE_CONFIG_DATA` (base64-encoded kubeconfig for deployment)


## Local Development

### Using Virtual Environment

```bash
# Clone the repository
git clone https://github.com/gavilugron/book-catalog.git
cd book-catalog

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

The API will be available at [http://127.0.0.1:8000/api/books/](http://127.0.0.1:8000/api/books/).

### Using Docker Compose

```bash
# Start all services (app + PostgreSQL)
docker-compose up --build
```

**Services:**

- **Application**: Available at `localhost:8000`
- **PostgreSQL Database**: Running as `db` service with persistent volume

To stop all services:

```bash
docker-compose down
```


## API Usage

Base URL: `http://localhost:8000/api/`

### Endpoints

| Method | Endpoint | Description |
| :-- | :-- | :-- |
| GET | `/api/books/` | List all books |
| GET | `/api/books/{id}/` | Get specific book details |
| POST | `/api/books/` | Create a new book |
| PUT | `/api/books/{id}/` | Update existing book |
| DELETE | `/api/books/{id}/` | Delete a book |
| GET | `/health/` | Health check endpoint |

### Examples

**List all books:**

```bash
curl http://localhost:8000/api/books/
```

**Get a specific book:**

```bash
curl http://localhost:8000/api/books/1/
```

**Create a new book:**

```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Dune",
    "author": "Frank Herbert",
    "isbn": "978-0-441-17271-9",
    "published_date": "1965-08-01"
  }'
```

**Update a book:**

```bash
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Dune Messiah"}'
```

**Delete a book:**

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```


## Testing

The project includes comprehensive test coverage using pytest.

**Run tests locally:**

```bash
# In virtual environment
pytest

# Using Docker
docker-compose run --rm app pytest
```

**Test Configuration:**

- Test files located in `api/tests/`
- Django settings configured in `pytest.ini`
- Automatic test execution in CI/CD pipeline


## Docker

### Building Images

**Build locally:**

```bash
docker build -t ghcr.io/gavilugron/book-catalog:latest .
```

**Push to GitHub Container Registry:**

```bash
docker push ghcr.io/gavilugron/book-catalog:latest
```


### Docker Features

- Multi-stage build optimization
- Health checks for container monitoring
- Non-root user for security
- Efficient layer caching
- Production-ready entrypoint script


## CI/CD Pipelines

The project includes three GitHub Actions workflows:

### 1. Test Workflow (`.github/workflows/test.yml`)

- Triggers on push/PR to `main`
- Runs database migrations
- Executes full test suite with pytest
- Reports test coverage


### 2. Build Workflow (`.github/workflows/ci-build.yml`)

- Builds Docker images using Buildx
- Pushes images to GitHub Container Registry
- Tags images with commit SHA and `latest`
- Multi-platform support


### 3. Deploy Workflow (`.github/workflows/ci-deploy.yml`)

- Decodes Kubernetes configuration
- Updates Helm chart with new image tags
- Deploys to Kubernetes cluster
- Integrates with ArgoCD for GitOps


## Kubernetes Deployment

The project supports multiple Kubernetes deployment strategies:

### Helm Chart Deployment

**Using the included Helm chart:**

```bash
# Deploy to default namespace
helm upgrade --install book-catalog ./books-catalog-chart \
  --namespace default \
  --set image.repository=ghcr.io/gavilugron/book-catalog \
  --set image.tag=latest
```

**Helm Chart Features:**

- Configurable replica count
- Resource limits and requests
- Ingress configuration
- Secret management
- Environment variable injection
- Database connection configuration


### Raw Kubernetes Manifests

**Deploy using raw manifests:**

```bash
# Deploy PostgreSQL
kubectl apply -f k8s_yamls/postgres/

# Deploy application
kubectl apply -f k8s_yamls/application/
```

**Manifest Structure:**

- **Application**: Deployment, Service, Ingress, Jobs, Secrets
- **PostgreSQL**: StatefulSet, Services, ConfigMaps, PersistentVolumes
- **DevOps Tools**: Additional charts and configurations


### ArgoCD GitOps

**ArgoCD Application Configuration:**

- Automated sync from Git repository
- Helm chart deployment
- Self-healing capabilities
- Rollback support

**Deploy ArgoCD Application:**

```bash
kubectl apply -f argocd/argocd-app.yaml
```

**GitOps Features:**

- Declarative configuration management
- Automated deployment on Git changes
- Visual deployment monitoring
- Rollback and recovery capabilities


## Project Structure

```
book-catalog/
├── .github/
│   ├── actions/install-dependencies/     # Reusable GitHub Actions
│   └── workflows/                        # CI/CD pipeline definitions
├── api/                                  # Django API application
│   ├── migrations/                       # Database migrations
│   ├── tests/                           # Test suite
│   └── [models, views, serializers]     # API implementation
├── argocd/                              # ArgoCD GitOps configurations
├── bookcatalog/                         # Django project settings
├── books-catalog-chart/                 # Helm chart
│   ├── templates/                       # Kubernetes templates
│   └── values.yaml                      # Chart configuration
├── k8s_yamls/                          # Raw Kubernetes manifests
│   ├── application/                     # Application manifests
│   ├── postgres/                        # PostgreSQL manifests
│   └── devops-chart/                    # Additional DevOps tools
├── docker-compose.yml                   # Local development setup
├── Dockerfile                          # Container definition
├── requirements.txt                     # Python dependencies
└── entrypoint.sh                       # Container entrypoint script
```


## Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch from `main`
3. **Make** your changes with appropriate tests
4. **Commit** using [Conventional Commits](https://www.conventionalcommits.org/)
5. **Submit** a Pull Request with detailed description

**Development Guidelines:**

- Follow PEP 8 coding standards
- Add tests for new features
- Update documentation as needed
- Ensure CI/CD pipeline passes

## License

This project is licensed under the MIT License. See the LICENSE file for details.

**About**: CCT-DevOps 2025 Summer Course - Book Catalog API

This project serves as a comprehensive example of modern DevOps practices, demonstrating the integration of development, containerization, orchestration, and GitOps methodologies in a production-ready application.
