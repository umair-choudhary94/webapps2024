from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password
# Create your views here.
from .models import *
def login_now(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
                # Login the user
                login(request, user)
                return redirect('welcome')
        
    return render(request, 'register/login.html')
def logout_view(request):
    logout(request)
    return redirect('home')
def register_now(request):
    if request.method == 'POST':
      
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        currency = request.POST['currency']
        hashed_password = make_password(password)

      
        user = Userprofile(user_name=username,currency=currency,email=email, password=hashed_password,first_name=first_name,last_name=last_name)
        
        user.save()
        
        return redirect('login') 

    return render(request, 'register/register.html')
def welcome_page(request):
    return render(request, 'register/welcomepage.html')