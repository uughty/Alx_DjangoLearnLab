from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your custom views
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
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += [
    path('posts/', PostListView.as_view(), name='post-list'),  # This one is fine as plural
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # singular 'post' here
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # singular 'post'
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # singular + 'update' instead of 'edit'
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # singular + delete
   path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

