from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view(), name='author_list_create'),
    path('authors/<int:id>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<int:id>/books/', views.AuthorBooksView.as_view(), name='author_books'),
]