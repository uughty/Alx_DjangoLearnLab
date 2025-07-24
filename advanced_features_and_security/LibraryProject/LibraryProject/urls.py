from django.urls import path

from . import views 

urlpatterns = [
    path('edit/', views.edit_view, name='edit'),
    path('create/', views.create_view, name='create'),
    path('view/', views.view_content, name='view'),
]
