from rest_framework import generics
from .models import *
from .serializers import *


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookCopiesView(generics.ListAPIView):
    serializer_class = BookCopySerializer

    def get_queryset(self):
        book_id = self.kwargs['id']
        return BookCopy.objects.filter(book__id=book_id)


class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer


class BookCopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    lookup_field = 'id'


# Book Lending Views
class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer


class BookLendingDetailView(generics.RetrieveAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer
    lookup_field = 'id'


class BookLendingReturnView(generics.UpdateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer


class OverdueLendingView(generics.ListAPIView):
    serializer_class = BookLendingSerializer

    def get_queryset(self):
        return BookLending.objects.filter(status='overdue')