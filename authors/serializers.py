from django.utils import timezone
from rest_framework import serializers
from .models import *
from books.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality', 'books_count']
        read_only_fields = ['id', 'books_count']

    def validate_birth_date(self, value):
        if value is None:
            raise serializers.ValidationError("Birth date cannot be null.")
        if value > timezone.now().date():
            raise serializers.ValidationError("Birth date cannot be in the future.")
        return value

    def validate(self, data):
        if not data.get('first_name'):
            raise serializers.ValidationError({"first_name": "This field cannot be blank."})
        if not data.get('last_name'):
            raise serializers.ValidationError({"last_name": "This field cannot be blank."})
        return data

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)
        author.books_count = Book.objects.filter(authors=author).count()
        author.save()
        return author


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')
