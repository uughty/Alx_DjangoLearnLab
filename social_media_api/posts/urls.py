from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import feed
from .views import FollowUserView, UnfollowUserView
from .views import FeedView
from . import views



router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'), 
     path("like/<int:pk>/", views.like_post, name="like_post"),
    path("unlike/<int:pk>/", views.unlike_post, name="unlike_post"),
]
