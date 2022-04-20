from yaml import serialize
from rest_framework import generics

from books.models import Book

from todos.models import Todo

from .serializers import BookSerializer

# Book API
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Todo API
