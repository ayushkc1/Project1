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
from django.db import connections
from django.utils import timezone

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@login_required(login_url="/login")
def index(request):
    # books = Book.objects.all()
    with connections["default"].cursor() as cursor:
        cursor.execute("SELECT * FROM libraryapp_Book")
        books = cursor.fetchall()
    print("Called?")
    print(len(books))
    return render(request, "libraryapp/home.html", {"books": books})


@login_required(login_url="/login")
def issue(request):
    if request.method == "POST":
        action = request.POST.get("action")
        print(action)
        if action == "search":
            book_name = request.POST["book_name"]
            print(book_name)
            try:
                # book1 = Book.objects.get(title=book_name)
                # print(type(book1))
                with connections["default"].cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM libraryapp_Book WHERE title = %s", [book_name]
                    )
                    books = cursor.fetchall()
                    for row in books:
                        print(row[0])
                        book = Book(
                            book_id=row[0], title=row[1], author=row[2], count=row[3]
                        )  # creating a book object
                        print(book, type(book))
                print(type(book))

            except Book.DoesNotExist:
                messages.error(request, "Book not found")
                return redirect("issue")

            return render(request, "libraryapp/issue.html", {"book": book})

        if action == "issue":
            book_id = request.POST.get("book_id")  # Assuming "book_id" is the name of the input field in the form
            if book_id:
                with connections["default"].cursor() as cursor:
                    print("user id ", request.user.id)
                    cursor.execute(
                        "SELECT * FROM libraryapp_book WHERE book_id = %s", [book_id]
                    )
                    row = cursor.fetchall()
                    print("here-change", row)
                    if row:
                        book = Book(
                            book_id=row[0][0], title=row[0][1], author=row[0][2], count=row[0][3]
                        )

                        if book.count > 0:
                            date_borrowed = date.today()
                            due_date = date.today() + timedelta(days=45)
                            borrow_id = random.randint(100000, 999999)
                            print("checkpoint-1",borrow_id, book, request.user.id, date_borrowed, due_date)

                            with connections["default"].cursor() as cursor:
                                cursor.execute(
                                    "INSERT INTO libraryapp_borrow (borrow_id, book_id, user_id, date_borrowed, due_date, deposit) VALUES (%s, %s, %s, %s, %s, %s)",
                                    [borrow_id, book_id, request.user.id, date_borrowed, due_date, 500],
                                )

                            book.count -= 1
                            # book.save()
                            messages.success(request, "Book issued successfully")
                        else:
                            messages.error(request, "Book is out of stock")
                    else:
                        messages.error(request, "Invalid book ID")
            else:
                messages.error(request, "No book ID provided")

            return redirect("renew")

    return render(request, "libraryapp/issue.html")


def renew(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    with connections['default'].cursor() as cursor:
        cursor.execute(
            "SELECT * FROM libraryapp_borrow AS b INNER JOIN libraryapp_book AS bo ON b.book_id=bo.book_id WHERE user_id = %s",
            [request.user.id],
        )
        rows = cursor.fetchall()
    borrowed_books=[]
    for row in rows:
                        print("here see",row)
                       
                        rem = -(date.today() - row[1]).days+7
                       
                        b = dict(
                            borrow_id=row[0], book_id=row[6], user_id=row[4], date_borrowed=row[1], due_date=row[2],title=row[7],days_remained=rem
                        ) 
                       
                        borrowed_books.append(b)
   # print(rows, type(rows))
    #print(borrowed_books, type(borrowed_books))
    context = {"borrowed_books": borrowed_books}
    return render(request, "libraryapp/renew.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            # Display an error message.
            return HttpResponse("Wrong")
    else:
        return render(request, "libraryapp/login.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get("password1")

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)

            # redirect user to home page
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "libraryapp/register.html", {"form": form})


def profile(request):
    with connections["default"].cursor() as cursor:
        cursor.execute(
            "SELECT * FROM libraryapp_borrow AS b INNER JOIN libraryapp_book AS bo ON b.book_id=bo.book_id WHERE user_id = %s",
            [request.user.id],
        )
        rows = cursor.fetchall()
    
    # print("username ", request.user)
    borrowed_books = []
    for row in rows:
        book_data = Book(book_id=row[6], title=row[7], author=row[8], count=row[9])
        # book_data = {
        #     'book_name':row[7],
        #     'book_author': row[8],
        #     'book_id':row[6],
        #     'borrow_id':row[0],
        # }
        borrowed=Borrow(borrow_id=row[0],date_borrowed=row[1], due_date=row[2],book_id=book_data,user_id=request.user,deposit=row[5] )
        borrowed_books.append(borrowed)
        
    
    context = {'borrowed_books': borrowed_books}
    return render(request, 'libraryapp/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect("/login?next=/")


def return_book(request, book_id, borrow_id):
    with connections['default'].cursor() as cursor:

        
        # Update book count and delete borrow record
        cursor.execute("UPDATE libraryapp_book SET count=count+1 WHERE book_id=%s",[book_id])
        cursor.execute("DELETE FROM libraryapp_borrow WHERE borrow_id=%s",[borrow_id])
    messages.success(request,"Book returned successfully")
    return redirect('renew')
        

# def pay_fine(request)
