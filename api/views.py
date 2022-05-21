from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model


from books.models import Book
from todos.models import Todo
from posts.models import Post


from .serializers import BookSerializer, TodoSerializer, PostSerializer, UserSerializer
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
class PostViewSet(viewsets.ModelViewSet): #ModelViewset provides both list & detail views
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostListView(generics.ListCreateAPIView): # to create read-write API endpoint
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView): # to create read-write API endpoint    
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

    

 
# Users API 
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer