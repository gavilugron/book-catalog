# Book Catalog API

This project provides a simple REST API for managing a catalog of books. It is built with Django and Django REST Framework and includes automation for testing, building a Docker image and deploying to Kubernetes via Helm.

## API Endpoints
- `GET /api/books/` – list all books
- `POST /api/books/` – create a book
- `GET /api/books/{id}/` – retrieve a book
- `PUT /api/books/{id}/` – update a book
- `DELETE /api/books/{id}/` – delete a book

## Local Development
1. Install Docker and Docker Compose.
2. Run `docker-compose up --build` to start the web app and PostgreSQL database.
3. The API will be available at `http://localhost:8000/api/books/`.

## Running Tests
Execute the Django tests locally using:
```bash
python manage.py test tests
```

## CI/CD Pipeline
GitHub Actions workflows automate testing, Docker image build and deployment.
- **ci-test.yml** – installs dependencies, runs migrations and tests using PostgreSQL.
- **ci-build.yml** – builds and pushes the Docker image when tests succeed.
- **ci-deploy.yml** – deploys the image to Kubernetes using Helm.

## Kubernetes Deployment with Helm
A simple Helm chart is included under `helm/`. To deploy:
```bash
helm upgrade --install book-catalog helm/ \
  --set image.repository=<your-docker-user>/book-catalog \
  --set image.tag=latest
```
Ensure your cluster credentials are configured beforehand.
