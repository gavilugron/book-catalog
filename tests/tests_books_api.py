from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create one book to test list/retrieve/update/delete
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            isbn="1111111111111",
            published_date="1949-06-08"
        )
        self.list_url = reverse('book-list')      # '/api/books/'
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])  # '/api/books/{pk}/'

    def test_list_books(self):
        """GET /api/books/ returns our existing book."""
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['title'], "1984")

    def test_create_book(self):
        """POST /api/books/ creates a new book."""
        payload = {
            "title": "Dune",
            "author": "Frank Herbert",
            "isbn": "2222222222222",
            "published_date": "1965-06-01"
        }
        resp = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(isbn="2222222222222").title, "Dune")

    def test_update_book(self):
        """PUT /api/books/{id}/ updates an existing book."""
        payload = {
            "title": "Nineteen Eighty-Four",
            "author": "G. Orwell",
            "isbn": "1111111111111",
            "published_date": "1949-06-08"
        }
        resp = self.client.put(self.detail_url(self.book.pk), payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")
        self.assertEqual(self.book.author, "G. Orwell")

    def test_delete_book(self):
        """DELETE /api/books/{id}/ removes the book."""
        resp = self.client.delete(self.detail_url(self.book.pk))
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())