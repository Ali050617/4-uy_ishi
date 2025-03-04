from django.contrib import admin
from .models import Author, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'nationality')
    search_fields = ('first_name', 'last_name', 'nationality')
    list_filter = ('nationality',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
