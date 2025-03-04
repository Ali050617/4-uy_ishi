from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'genre', 'isbn',
                  'published_date', 'description', 'page_count', 'language')

    def create(self, validated_data):
        authors = validated_data.pop('authors', [])
        genre = validated_data.pop('genre')
        book = Book.objects.create(genre=genre, **validated_data)
        book.authors.set(authors)

        return book


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ('id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date')


class BookLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = ('id', 'book_copy', 'borrower_name', 'borrower_email',
                  'borrowed_date', 'due_date', 'returned_date', 'status')
