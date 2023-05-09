from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# @login_required(login_url='/login')
def index(request):
    return render(request, 'libraryapp/home.html')

# @login_required(login_url='/login')
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def issue(request):
    return render(request, 'libraryapp/issue.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            # Display an error message.
            return HttpResponse("Wrong")
    else:
        return render(request, 'libraryapp/login.html')