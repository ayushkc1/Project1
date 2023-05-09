from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @login_required(login_url='/login')
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Display an error message.
            return render(request, 'login.html', {'error': 'Invalid login credentials.'})
    else:
        return render(request, 'login.html')