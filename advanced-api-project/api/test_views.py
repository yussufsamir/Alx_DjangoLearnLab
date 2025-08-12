from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author





class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name='George Orwell')
        self.book = Book.objects.create(title='1984', publication_year=1949, author=self.author)

    def test_create_book(self):
        url = reverse('book-create')  # Use 'book-create' for POST
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Animal Farm')
    # ...existing code...
    def test_update_book(self): 
        url = reverse('book-update')  # No pk argument
        data = {'title': 'Nineteen Eighty-Four'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Nineteen Eighty-Four')

    def test_delete_book(self):
        url = reverse('book-delete')  # No pk argument
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
    # ...existing code...


    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=1984'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_order_books_by_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
