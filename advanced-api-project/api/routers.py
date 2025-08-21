from rest_framework.routers import DefaultRouter
from .viewsets import BookViewSet  # if you have a ViewSet like this

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
