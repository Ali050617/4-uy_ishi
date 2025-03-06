from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
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
    list_display = (
    'book_copy', 'borrower_name', 'borrowed_date', 'due_date', 'returned_date', 'status', 'days_overdue_display')
    list_filter = ('status', 'due_date', 'returned_date')
    search_fields = ('borrower_name', 'borrower_email', 'book_copy__inventory_number', 'book_copy__book__title')
    ordering = ('-borrowed_date',)

    def days_overdue_display(self, obj):
        if obj.returned_date is None and obj.due_date < timezone.now().date():
            overdue_days = (timezone.now().date() - obj.due_date).days
            return format_html(f'<span style="color:red;">{overdue_days} kun</span>')
        return '-'

    days_overdue_display.short_description = "Overdue Kunlar"