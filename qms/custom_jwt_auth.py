from rest_framework_simplejwt.authentication import JWTAuthentication

from qms.serializers import AuthorSerializer

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Calling the parent class method to perform JWT authentication
        user, _ = super().authenticate(request)

        # fetching the user's data in the request's data with the user's information
        if user and hasattr(user, 'author'):
            author_serializer = AuthorSerializer(user.author)
            request.data['author'] = author_serializer.data

        return user, _