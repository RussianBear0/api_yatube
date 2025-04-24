from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('posts/<post_id>/comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
