from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # ✅ /register
    path('login/', LoginView.as_view(), name='login'),           # ✅ /login
    path('profile/', ProfileView.as_view(), name='profile'), 
        path("follow/<int:user_id>/", follow_user, name="follow-user"),
    path("unfollow/<int:user_id>/", unfollow_user, name="unfollow-user"),    # ✅ /profile
]
