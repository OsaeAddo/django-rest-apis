from django.urls import path

from .views import BookAPIView, DetailTodoView, ListTodoView

urlpatterns = [
    #Book API
    path('book/', BookAPIView.as_view()),

    # Todo API
    path('todo/', ListTodoView.as_view()),
    path('todo/<int:pk>/', DetailTodoView.as_view()),
]