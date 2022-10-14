from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Username or Password is Incorrect')
    
    return render(request,'login.html')


def user_register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created. Please Login to Continue..')
            return redirect('user_login')
    context = {
        'register_form' : form
    }
    return render(request,'register.html',context)

def user_logout(request):
    logout(request)
    return redirect('user_login')