from django.urls import path

from .views import BookAPIView, DetailTodoView, ListTodoView, PostListView, PostDetailView

urlpatterns = [
    #Book API
    path('book/', BookAPIView.as_view()),

    # Todo API
    path('todo/', ListTodoView.as_view()),
    path('todo/<int:pk>/', DetailTodoView.as_view()),

    #Posts API
    path('post/v1/', PostListView.as_view()), # v1 represents the API version, a good idea
    path('post/v1/<int:pk>/', PostDetailView.as_view()),
]