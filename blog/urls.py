'''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]'''

# blog/urls.py

from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDeleteView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
]

