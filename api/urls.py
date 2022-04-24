from django.urls import path

from .views import BookAPIView, DetailTodoView, ListTodoView, PostListView, PostDetailView

urlpatterns = [
    #Book API
    path('book/', BookAPIView.as_view()),

    # Todo API
    path('todo/', ListTodoView.as_view()),
    path('todo/<int:pk>/', DetailTodoView.as_view()),

    #Posts API
    path('posts/v1/', PostListView.as_view()),
    path('posts/v1/<int:pk>/', PostDetailView.as_view()),
]