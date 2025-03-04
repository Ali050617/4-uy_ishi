from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from django.utils.timezone import now
from rest_framework.response import Response

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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Kitob allaqachon qaytarilgan bo'lsa, statusni yangilashga ruxsat bermaymiz
        if instance.status == "returned":
            return Response({"detail": "This book has already been returned."}, status=status.HTTP_400_BAD_REQUEST)

        # Qaytarilgan sanani hozirgi vaqtga o'zgartiramiz
        instance.returned_date = now()
        instance.status = "returned"
        instance.save()

        # Yangilangan ma'lumotni qaytaramiz
        return Response(BookLendingSerializer(instance).data, status=status.HTTP_200_OK)


class OverdueLendingView(generics.ListAPIView):
    serializer_class = BookLendingSerializer

    def get_queryset(self):
        return BookLending.objects.filter(status='overdue')