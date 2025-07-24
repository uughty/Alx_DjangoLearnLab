from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Form handling to create a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    # Form handling to edit a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    # Form handling to delete a book
    pass
