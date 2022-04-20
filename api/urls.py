from django.urls import path

from .views import BookAPIView, DetailTodoView, ListTodoView

urlpatterns = [
    path('book/', BookAPIView.as_view()),
    path('todo/', ListTodoView.as_view()),
    path('todo/<int:pk>/', DetailTodoView.as_view()),
]