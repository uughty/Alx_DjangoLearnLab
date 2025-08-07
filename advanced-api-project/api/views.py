from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters  # ✅ Needed for filtering

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrEditor  # Custom permission

# Custom FilterSet for Book model (optional, but useful if doing complex filtering later)
class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# Anyone can read (with filtering, search, and ordering now)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Add filtering, searching, ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_class = BookFilter  # ✅ Hooking custom filter
    search_fields = ['title', 'author']  # ✅ For search
    ordering_fields = ['title', 'author', 'publication_year']  # ✅ For ordering

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Only authenticated users can create
class CreateView(generics.CreateAPIView):  # Must be named CreateView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Only Admins or Editors can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrEditor]

# Only Admins or Editors can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrEditor]
