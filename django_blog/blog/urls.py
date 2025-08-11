from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,
    SearchResultsView,
    RegisterView,
    ProfileView,
)

urlpatterns = [
    # Blog posts CRUD
    path('', PostListView.as_view(), name='post-list'),
    path('posts/', PostListView.as_view(), name='post-list'),  # optional plural path
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments CRUD
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Tag filtering
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # Search
    path('search/', SearchResultsView.as_view(), name='post-search'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
     path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
urlpatterns += [
    path('posts/', PostListView.as_view(), name='post-list'),  # This one is fine as plural
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # singular 'post' here
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # singular 'post'
    
]

