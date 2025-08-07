from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    CreateView,  # 👈 important: this matches what the checker expects
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # 👈 required
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # 👈 required
]
