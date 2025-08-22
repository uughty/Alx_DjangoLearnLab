from django.contrib import admin
from django.urls import path, include
from . import health



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')), 
     path('api/', include('posts.urls')), # ✅ includes accounts URLs
     path("health/", health),
]
