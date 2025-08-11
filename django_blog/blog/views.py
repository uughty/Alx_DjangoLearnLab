from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            user.email = email
            user.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Email cannot be empty.")
    return render(request, "blog/profile.html", {"user": user})
