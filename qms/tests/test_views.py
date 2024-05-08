from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from qms.models import Author, Quote
from django.contrib.auth.models import User

class CreateUserAPIViewTestCase(TestCase):
    def test_create_user(self):
        """Test creating a new user/author"""
        client = APIClient()
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        url = reverse('create-user')
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Author.objects.count(), 1)

class ListQuotesAPIViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(user=self.user)
        self.quote1 = Quote.objects.create(text='Test Quote 1', author=self.author)
        self.quote2 = Quote.objects.create(text='Test Quote 2', author=self.author)

    def test_list_quotes(self):
        """Test retrieving a list of all quotes"""
        client = APIClient()
        url = reverse('list-quotes')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class CreateQuoteAPIViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(user=self.user)

    def test_create_quote(self):
        """Test creating a new quote"""
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {'text': 'Test Quote'}
        url = reverse('create-quote')
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quote.objects.count(), 1)
        self.assertEqual(Quote.objects.get().text, 'Test Quote')
        self.assertEqual(Quote.objects.get().author, self.author)

class RetrieveQuoteAPIViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(user=self.user)
        self.quote = Quote.objects.create(text='Test Quote', author=self.author)

    def test_retrieve_quote(self):
        """Test retrieving a specific quote"""
        client = APIClient()
        url = reverse('retrieve-quote', args=[self.quote.id])
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Test Quote')

class DeleteQuoteAPIViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(user=self.user)
        self.quote = Quote.objects.create(text='Test Quote', author=self.author)

    def test_delete_quote(self):
        """Test deleting a quote"""
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('delete-quote', args=[self.quote.id])
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Quote.objects.count(), 0)

    def test_delete_quote_unauthorized(self):
        """Test deleting a quote without authentication"""
        client = APIClient()
        url = reverse('delete-quote', args=[self.quote.id])
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_quote_not_owner(self):
        """Test deleting a quote that the user doesn't own"""
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        other_author = Author.objects.create(user=other_user)
        other_quote = Quote.objects.create(text='Other Quote', author=other_author)
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('delete-quote', args=[other_quote.id])
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class UpdateQuoteAPIViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(user=self.user)
        self.quote = Quote.objects.create(text='Test Quote', author=self.author)

    def test_update_quote(self):
        """Test updating a quote"""
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {'text': 'Updated Quote'}
        url = reverse('update-quote', args=[self.quote.id])
        response = client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.quote.refresh_from_db()
        self.assertEqual(self.quote.text, 'Updated Quote')

    def test_update_quote_unauthorized(self):
        """Test updating a quote without authentication"""
        client = APIClient()
        data = {'text': 'Updated Quote'}
        url = reverse('update-quote', args=[self.quote.id])
        response = client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_quote_not_owner(self):
        """Test updating a quote that the user doesn't own"""
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        other_author = Author.objects.create(user=other_user)
        other_quote = Quote.objects.create(text='Other Quote', author=other_author)
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {'text': 'Updated Quote'}
        url = reverse('update-quote', args=[other_quote.id])
        response = client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

