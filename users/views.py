from django.shortcuts import render, redirect
from .models import CustomerUser
from django.contrib.auth import login, logout
from .forms import AuthUserForm, CreateUserForm

def login_user(request):
    if request.method == 'POST':
        form = AuthUserForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthUserForm(request)
    return render(request, 'users/login.html', {'form': form})



def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')