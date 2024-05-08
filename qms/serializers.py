from rest_framework import serializers
from .models import Quote, Author
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['pen_name', 'date_of_birth']


class UserSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'author']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)
        user = User.objects.create_user(**validated_data)
        if author_data:
            Author.objects.create(user=user, **author_data)
        else:
            Author.objects.create(user=user)
        return user


class QuoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, required=False)

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'source', 'creation_date']
