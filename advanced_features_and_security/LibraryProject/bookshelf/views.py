from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def view_dashboard(request):
    return HttpResponse("Viewing dashboard.")

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_item(request):
    return HttpResponse("Item created.")

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_item(request):
    return HttpResponse("Item edited.")

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_item(request):
    return HttpResponse("Item deleted.")
