from django.contrib import admin
from .models import Book, BookCopy, BookLending


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'published_date', 'language')
    search_fields = ('title', 'isbn', 'authors__first_name', 'authors__last_name')
    list_filter = ('language', 'published_date')


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'inventory_number', 'condition', 'is_available', 'added_date')
    search_fields = ('inventory_number', 'book__title')
    list_filter = ('condition', 'is_available')


@admin.register(BookLending)
class BookLendingAdmin(admin.ModelAdmin):
    list_display = ('book_copy', 'borrower_name', 'borrower_email', 'borrowed_date', 'due_date', 'status')
    search_fields = ('borrower_name', 'borrower_email', 'book_copy__book__title')
    list_filter = ('status', 'borrowed_date', 'due_date')
