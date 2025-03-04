from django.db import models
from authors.models import Genre
from authors.models import *


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.IntegerField()
    language = models.CharField(max_length=20)


class BookCopy(models.Model):

    CONDITION_CHOIS = [
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    inventory_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOIS, default='new')
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)


class BookLending(models.Model):

    STATUS_CHOIS = [
        ('ac', 'Active'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ]

    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrower_email = models.EmailField()
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOIS, default='ac')