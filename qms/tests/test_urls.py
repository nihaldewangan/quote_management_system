from django.test import SimpleTestCase
from django.urls import reverse, resolve
from qms.views import (
    CreateQuoteAPIView,
    ListQuotesAPIView,
    CreateUserAPIView,
    RetrieveQuoteAPIView,
    UpdateQuoteAPIView,
    DeleteQuoteAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class TestURLs(SimpleTestCase):

    def test_create_user_url_resolves(self):
        url = reverse('create-user')
        self.assertEqual(resolve(url).func.view_class, CreateUserAPIView)

    def test_list_quotes_url_resolves(self):
        url = reverse('list-quotes')
        self.assertEqual(resolve(url).func.view_class, ListQuotesAPIView)

    def test_create_quote_url_resolves(self):
        url = reverse('create-quote')
        self.assertEqual(resolve(url).func.view_class, CreateQuoteAPIView)

    def test_retrieve_quote_url_resolves(self):
        url = reverse('retrieve-quote', args=[1])
        self.assertEqual(resolve(url).func.view_class, RetrieveQuoteAPIView)

    def test_update_quote_url_resolves(self):
        url = reverse('update-quote', args=[1])
        self.assertEqual(resolve(url).func.view_class, UpdateQuoteAPIView)

    def test_delete_quote_url_resolves(self):
        url = reverse('delete-quote', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteQuoteAPIView)

    def test_token_obtain_pair_url_resolves(self):
        url = reverse('token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_refresh_url_resolves(self):
        url = reverse('token_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)
