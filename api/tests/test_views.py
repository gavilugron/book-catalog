import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Book

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_list_books(api_client):
    """
    GET /api/books/ should return 200 OK
    """
    url = reverse("api:book-list")
    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_health_check(api_client):
    """
    GET /api/health/ should return JSON {"status":"ok"}
    """
    url = reverse("api:health")
    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("status") == "ok"

@pytest.mark.django_db
def test_create_book(api_client):
    """
    POST /api/books/ should create a book and return 201 with the new object
    """
    url = reverse("api:book-list")
    payload = {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "published_date": "1949-06-08"
    }

    response = api_client.post(url, payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["isbn"] == payload["isbn"]
    assert Book.objects.filter(pk=data["id"]).exists()

@pytest.mark.django_db
def test_retrieve_book(api_client):
    """
    GET /api/books/{id}/ should return the correct book data
    """
    book = Book.objects.create(
        title="Brave New World",
        author="Aldous Huxley",
        isbn="9780060850524",
        published_date="1932-08-30"
    )

    url = reverse("api:book-detail", args=[book.id])
    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data["id"] == book.id
    assert data["title"] == book.title
    assert data["author"] == book.author
    assert data["isbn"] == book.isbn
    assert data["published_date"] == book.published_date
