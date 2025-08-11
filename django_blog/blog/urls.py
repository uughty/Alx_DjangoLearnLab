from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your custom views
from .views import PostSearchView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    # other views...
)

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,  # <-- make sure this is imported
    SearchResultsView,  # if you also have search
)
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Comments
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Tag filtering URL — THIS IS THE MISSING PART
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # Optionally search URL
    path('search/', SearchResultsView.as_view(), name='post-search'),
]
urlpatterns += [
    path('posts/', PostListView.as_view(), name='post-list'),  # This one is fine as plural
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # singular 'post' here
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # singular 'post'
    
]

