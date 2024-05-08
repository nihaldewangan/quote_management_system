"""
This module defines the Django REST API views for the Quote Management System (QMS) application.

The views include:
- CreateUserAPIView: Allows creating a new user/author.
- ListQuotesAPIView: Retrieves a list of all quotes.
- CreateQuoteAPIView: Allows creating a new quote, authenticated users only.
- RetrieveQuoteAPIView: Retrieves a specific quote.
- UpdateQuoteAPIView: Allows updating a quote, authenticated users only and only for quotes they own.
- DeleteQuoteAPIView: Allows deleting a quote, authenticated users only and only for quotes they own.
"""
from rest_framework import generics, permissions
from .models import Quote, Author
from .serializers import QuoteSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, IsAuthenticated

# create user/author
class CreateUserAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = UserSerializer

# list all quotes
class ListQuotesAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# create a quote
class CreateQuoteAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)

# retrieve a quote
class RetrieveQuoteAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# update a quote
class UpdateQuoteAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# delete a quote
class DeleteQuoteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
