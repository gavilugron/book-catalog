# import pytest
# from rest_framework.test import APIClient
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from api.models import Book

# class BookViewTest(APITestCase):
    
#     def test_response_is_correct(self):
#         book = Book.objects.create(
#             title="Demo",
#             description="Description",
#             author="Author"
#         )
        
#         url = reverse('api:book-list')
#         response = self.client.get(url, format='json')
#         assert response.status_code == status.HTTP_200_OK
#         body = response.json()
#         returned_book = body[0]
#         assert returned_book["title"] == book.title
#         assert returned_book["description"] == book.description
#         assert returned_book["author"] == book.author


# class HealthViewTest(APITestCase):
    
#     def test_response_is_correct(self):
#         url = reverse('api:health')
#         response = self.client.get(url, format='json')
#         assert response.status_code == status.HTTP_200_OK
#         body = response.json()
#         assert body['status'] == 'ok'
        
#     @pytest.mark.django_db
#     def test_create_book():
#         client = APIClient()
#         url = reverse("book-list")            # router name for the list/create endpoint
#         payload = {
#                 "title": "1984",
#                 "author": "George Orwell",
#                 "isbn": "9780451524935",
#                 "published_date": "1949-06-08"
#             }

#     response = client.post(url, payload, format="json")
#     assert response.status_code == 201    # Created
#     data = response.json()
#     # make sure the API echoes back what we sent
#     assert data["title"] == payload["title"]
#     assert data["author"] == payload["author"]
#     assert data["isbn"] == payload["isbn"]

#     # and the book really exists in the DB
#     assert Book.objects.filter(pk=data["id"]).exists()
    
#     @pytest.mark.django_db
#     def test_retrieve_book():
#         # first, create a Book directly in the DB
#         book = Book.objects.create(
#             title="Brave New World",
#             author="Aldous Huxley",
#             isbn="9780060850524",
#             published_date="1932-08-30"
#         )

#     client = APIClient()
#     url = reverse("book-detail", args=[book.id])   # router name for the retrieve endpoint
#     response = client.get(url)
#     assert response.status_code == 200

#     data = response.json()
#     # verify the returned JSON matches our book
#     assert data["id"] == book.id
#     assert data["title"] == book.title
#     assert data["author"] == book.author
#     assert data["isbn"] == book.isbn
    
    
    
    
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
