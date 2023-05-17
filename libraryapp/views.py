from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, Borrow
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import RegistrationForm
from datetime import date, timedelta
import random
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class UserAPIViewSingle(APIView):
    def get(self, request,pk):
        users = User.objects.get(pk=pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@login_required(login_url='/login')
def index(request):
  #  books = Book.objects.all()
    books=Book.objects.raw('SELECT * FROM libraryapp_book')
    print(books)
    print("Called?")
    print(len(books))
    return render(request, 'libraryapp/home.html', {'books': books})


@login_required(login_url='/login')
def issue(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        print(action)
        if action == 'search':
            book_name = request.POST['book_name']
            print(book_name)
            try:
                #book = Book.objects.get(title=book_name)
                #book = Book.objects.raw('SELECT * FROM libraryapp_book WHERE title = %s LIMIT 1;', [book_name])[0]

                book=Book.objects.raw('SELECT * FROM libraryapp_book WHERE title=%s',[book_name])[0]
                print(book)
            except Book.DoesNotExist:
                messages.error(request, 'Book not found')
                return redirect('issue')
            return render(request, 'libraryapp/issue.html', {'book': book})
        if action == "issue":
            book_id = request.POST['book_id']
            #book = Book.objects.get(book_id=book_id)
            book=Book.objects.raw('SELECT * FROM libraryapp_book WHERE book_id=%s',[book_id])[0]
            if book.count > 0:
                borrow = Borrow.objects.create(
                    book=book,
                    user=request.user,
                    due_date=date.today() + timedelta(days=7)
                )
            book.count -= 1
            book.save()
            messages.success(request, 'Book issued successfully')
        else:
            messages.error(request, 'Book is already issued')
        return redirect('issue')

    return render(request, 'libraryapp/issue.html')


def renew(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    if request.method == 'POST':
        book_id = request.POST['book_id']
       # book = Book.objects.get(book_id=book_id)
        book=Book.objects.raw('SELECT * FROM libraryapp_book WHERE book_id=%s',[book_id])[0]
       # borrows = Borrow.objects.filter(book=book, user=request.user)
        borrows = Borrow.objects.raw('SELECT * FROM libraryapp_borrow WHERE book_id = %s AND user_id = %s;', [book.book_id, request.user.id])

        for borrow in borrows:
            borrow.date_borrowed = date.today()
            borrow.save()
        messages.success(request, 'Book renewed successfully')
        return redirect('renew')
    context = {'borrowed_books': borrowed_books}
    return render(request, 'libraryapp/renew.html', context)


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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)

            # redirect user to home page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'libraryapp/register.html', {'form': form})


def profile(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    context = {'borrowed_books': borrowed_books}
    return render(request, 'libraryapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/login?next=/')   

def return_book(request, book_id, borrow_id):
    book = get_object_or_404(Book, pk=book_id)
    borrow = get_object_or_404(Borrow, pk=borrow_id, book=book, user=request.user)
    book.count += 1
    book.save()
    borrow.delete()
    messages.success(request, 'Book returned successfully')
    return redirect('/')
