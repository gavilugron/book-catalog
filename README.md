# Book Catalog API

This project provides a simple REST API for managing books using Django and the Django REST Framework.

## API Endpoints

- `GET /api/books/` – List all books
- `POST /api/books/` – Create a new book
- `GET /api/books/{id}/` – Retrieve a book
- `PUT /api/books/{id}/` – Update a book
- `DELETE /api/books/{id}/` – Delete a book

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

You can also use Docker for local development:

```bash
docker-compose up --build
```

## Running Tests

```bash
python manage.py test
```

## CI/CD

GitHub Actions workflows automatically run tests, build a Docker image and deploy a Helm release when changes are pushed to the `main` branch.

## Kubernetes Deployment

The Helm chart in `helm/` creates a Deployment, Service and optional Ingress for the application. Configure the container image by setting `image.repository` and `image.tag` values.

Example deployment:

```bash
helm upgrade --install book-catalog helm/ \
  --set image.repository=myuser/book-catalog \
  --set image.tag=latest
```
