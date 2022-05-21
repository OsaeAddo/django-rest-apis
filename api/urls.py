from django.urls import path
from rest_framework.routers import SimpleRouter


# from .views import BookAPIView, DetailTodoView, ListTodoView, PostListView, PostDetailView, UserDetail, UserList

# Using Routers and Viewsets
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')


urlpatterns = router.urls

# urlpatterns = [
#     # Users API
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>', UserDetail.as_view()),
    
#     #Book API
#     path('book/', BookAPIView.as_view()),

#     # Todo API
#     path('todo/', ListTodoView.as_view()),
#     path('todo/<int:pk>/', DetailTodoView.as_view()),

#     #Posts API
#     path('post/v1/', PostListView.as_view()), # v1 represents the API version, a good idea
#     path('post/v1/<int:pk>/', PostDetailView.as_view()),
# ]