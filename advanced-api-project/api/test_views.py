from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from library.models import Book


from rest_framework.authtoken.models import Token
class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.book = Book.objects.create(title='Dune', author='Frank Herbert', published_year=1965)

    def test_create_book(self):
        data = {'title': 'Neuromancer', 'author': 'William Gibson', 'published_year': 1984}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Neuromancer')

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        data = {'title': 'Dune Messiah'}
        response = self.client.patch(f'/api/books/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Dune Messiah')

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        Book.objects.create(title='1984', author='George Orwell', published_year=1949)
        response = self.client.get('/api/books/?author=Frank Herbert')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['author'], 'Frank Herbert')

    def test_permission_denied_without_auth(self):
        client = APIClient()  # No auth
        response = client.post('/api/books/', {'title': 'X', 'author': 'Y', 'published_year': 2000})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
