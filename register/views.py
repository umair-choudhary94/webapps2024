from django.shortcuts import render

# Create your views here.

def login_now(request):
    return render(request, 'register/login.html')