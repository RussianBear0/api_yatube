from django.urls import include, path

from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PostViewSet, CommentViewSet

#Роутер
router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('posts/<post_id>/comments', CommentViewSet)

urlpatterns = [
    #Роутер
    path('v1/', include(router.urls)),
]