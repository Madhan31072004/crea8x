from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserDetails
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash password
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')  # Redirect to login page
  # Redirect to login page

    else:
        form = RegistrationForm()
    
    return render(request, "register.html", {"form": form})
