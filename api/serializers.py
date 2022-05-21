from rest_framework import serializers

from books.models import Book
from todos.models import Todo
from posts.models import Post


#Book API 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')


# Todo API
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body')


# Blog Posts API
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','author', 'title', 'body', 'created_at')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')