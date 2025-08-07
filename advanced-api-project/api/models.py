from django.db import models

# Author model stores the name of each author.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model stores book details and links to an Author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
# Author model stores the name of each author.
# Each author can have multiple books (one-to-many relationship).
class Author(models.Model):
    ...
    
# Book model stores book details.
# Each book is linked to a single author using a ForeignKey.
class Book(models.Model):
    ...
