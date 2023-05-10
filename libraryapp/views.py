from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, Borrow

# def index(request):
#     return render(request, 'libraryapp/home.html')
from django.contrib.auth.models import User, auth

# @login_required(login_url='/login')
def index(request):
    return render(request, 'libraryapp/home.html')

# @login_required(login_url='/login')
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def issue(request):
    return render(request, 'libraryapp/issue.html')

def index(request):
    books = Book.objects.all()
    print("Called?")
    print(len(books))
    return render(request, 'libraryapp/home.html', {'books': books})


def issue_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        Borrow.objects.create(
            book=book,
            user=request.user,
            due_date=request.POST['due_date']
        )
        return HttpResponseRedirect(reverse('book_detail', args=(book.id,)))
    return render(request, 'libraryapp/issue.html', {'book': book})

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