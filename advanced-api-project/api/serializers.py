from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer includes the author's name and a nested BookSerializer for related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
# BookSerializer handles serialization of Book model fields.
# It includes a custom validator to ensure publication_year is not in the future.

# AuthorSerializer serializes the author's name and includes a nested
# BookSerializer to display all related books (reverse one-to-many).
