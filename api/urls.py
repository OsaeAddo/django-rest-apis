from django.urls import path

from .views import BookAPIView

urlpatterns = [
    path('book/', BookAPIView.as_view()),
]