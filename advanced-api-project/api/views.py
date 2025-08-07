from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# 🔹 List and Create Books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create, everyone can read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# 🔹 Retrieve, Update, Delete a Single Book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can update or delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# BookListCreateView handles GET for listing all books,
# and POST for creating a new book. Authenticated users can create.
# Everyone (even unauthenticated users) can view the list.

# BookRetrieveUpdateDestroyView handles GET, PUT, PATCH, DELETE for a single book.
# Only authenticated users can modify or delete.
