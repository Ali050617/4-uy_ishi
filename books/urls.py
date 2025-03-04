from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/<int:id>/copies/', views.BookCopiesView.as_view(), name='book_copies'),
    path('copies/', views.BookCopyListCreateView.as_view(), name='book_copy_list_create'),
    path('copies/<int:id>/', views.BookCopyDetailView.as_view(), name='book_copy_detail'),
    path('lendings/', views.BookLendingListCreateView.as_view(), name='book_lending_list_create'),
    path('lendings/<int:id>/', views.BookLendingDetailView.as_view(), name='book_lending_detail'),
    path('lendings/<int:id>/return/', views.BookLendingReturnView.as_view(), name='book_lending_return'),
    path('lendings/overdue/', views.OverdueLendingView.as_view(), name='overdue_lending'),
]