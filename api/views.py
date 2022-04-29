from rest_framework import generics

from books.models import Book
from todos.models import Todo
from posts.models import Post


from .serializers import BookSerializer, TodoSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly


# Book API
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Todo API
class ListTodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodoView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



# Blog Post API
class PostListView(generics.ListCreateAPIView): # to create read-write API endpoint
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView): # to create read-write API endpoint    
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer