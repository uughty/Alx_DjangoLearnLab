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
    # other views...
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
     path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

urlpatterns += [
    path('posts/', PostListView.as_view(), name='post-list'),  # This one is fine as plural
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # singular 'post' here
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # singular 'post'
    
]

