from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Book
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .forms import OptionsForm, BookForm, UserForm
from django.db.models import Count

def is_float(s):
    """Check if a value is a float"""
    try:
        float(s)
        return True
    except ValueError:
        return False
    

def getCheckboxForm():
    """Create form with all book names"""
    books = Book.objects.all().values_list('pk', 'name')
    choices = [(pk, name) for pk, name in books]
    form = OptionsForm()
    form.fields['options'].choices = choices
    return form

@csrf_exempt
def index(request):
    """Render books page"""
    books = Book.objects.all()
    context = {
        'books': books,
        'checkboxForm': getCheckboxForm()
    }
    return render(request, 'booksPage.html', context)

@csrf_exempt
def users_page(request):
    """Render users page"""
    
    users = User.objects.all()
    context = {
        'users': users,
        'checkboxForm': getCheckboxForm()
    }
    return render(request, 'usersPage.html', context)



@csrf_exempt
def book_filter(request):
    """Return books based on constraints"""
    if request.method == 'POST':
        key = str(request.POST.get('key'))
        constraint = str(request.POST.get('constraint'))
        value = str(request.POST.get('value')).strip()
        if key == 'name': # handle constraints about names
            if constraint == '<':
                books = Book.objects.filter(name__lt=value).order_by('name')
            elif constraint == '>':
                books = Book.objects.filter(name__gt=value).order_by('name')
            else:
                books = Book.objects.filter(name=value).order_by('name')

        else: # handle constraints about price
            if not is_float(value):
                return render(request, 'booksPage.html', {}) # should add more error messages

            if constraint == '<':
                books = Book.objects.filter(price__lt=value).order_by('name')
            elif constraint == '>':
                books = Book.objects.filter(price__gt=value).order_by('name')
            else:
                books = Book.objects.filter(price=value).order_by('name')

    else:
        books = Book.objects.all()
    context = {
        'books': books,
        'checkboxForm': getCheckboxForm()
    }
    return render(request, 'booksPage.html', context)
                
            

@csrf_exempt
def user_filter(request):
    """Return users based on constraints"""
    if request.method == 'POST':
        key = str(request.POST.get('key'))
        constraint = str(request.POST.get('constraint'))
        value = str(request.POST.get('value')).strip()

        if key == 'userName': # handle constraints about names
            if constraint == '<':
                users = User.objects.filter(name__lt=value).order_by('name')
            elif constraint == '>':
                users = User.objects.filter(name__gt=value).order_by('name')
            else:
                users = User.objects.filter(name=value).order_by('name')
            
        elif key == 'age': # handle constraints about age
            if constraint == '<':
                users = User.objects.filter(age__lt=value).order_by('name')
            elif constraint == '>':
                users = User.objects.filter(age__gt=value).order_by('name')
            else:
                users = User.objects.filter(age=value).order_by('name')
        else: # handle constraints about number of books
            if not is_float(value):
                return render(request, 'booksPage.html', {})
            if constraint == '<':
                users = User.objects.annotate(num_liked_books=Count('liked_books')).filter(num_liked_books__lt=value)
            elif constraint == '>':
                users = User.objects.annotate(num_liked_books=Count('liked_books')).filter(num_liked_books__gt=value)
            else:
                users = User.objects.annotate(num_liked_books=Count('liked_books')).filter(num_liked_books=value)
    else:
        users = User.objects.all()
    context = {
        'users': users,
        'checkboxForm': getCheckboxForm()
    }
    return render(request, 'usersPage.html', context)



@csrf_exempt
def user_alt_filter(request):
    """Return users who have read certain books"""
    if request.method == 'POST':
        selected_book_pks = request.POST.getlist('options')
        selected_books = Book.objects.filter(pk__in=selected_book_pks).values_list('name', flat=True)
        selected_book_names = list(selected_books)
        books = Book.objects.filter(name__in=selected_book_names)
        users = User.objects.filter(liked_books__in=books).distinct()
        context = {
            'users': users,
            'checkboxForm': getCheckboxForm()
        }
        return render(request, 'usersPage.html', context)
            
    return users_page(request)


@csrf_exempt
def delete_book(request, pk):
    """Delete the book"""
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return(index(request))

@csrf_exempt
def delete_user(request, pk):
    """Delete the user"""
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.delete()
    return users_page(request)


@csrf_exempt
def add_book(request):
    """Create new book"""
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        if name and price:
            if is_float(price):
                book = Book(name=name, price=price)
                book.save() 
            # should add error catching
    return index(request)


@csrf_exempt
def add_user(request):
    """Create new user"""
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        liked_books_pks = request.POST.getlist('options')
        if name and age and liked_books_pks:
            # create the new user
            new_user = User.objects.create(name=name, age=int(age))

            # associate the liked books
            liked_books = Book.objects.filter(pk__in=liked_books_pks)
            new_user.liked_books.set(liked_books)
        
    return users_page(request)

@csrf_exempt
def update_book(request, pk):
    """Update book information when edited"""
    if request.method =='POST':
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()

    return index(request)


@csrf_exempt
def update_user(request, pk):
    """Update user information when edited"""
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        liked_books_pks = request.POST.getlist('options')
        print(liked_books_pks)
        user = User.objects.get(id=pk)
        user.name = name
        user.age = age
        user.save()
        user.liked_books.set(liked_books_pks)
    return users_page(request)
        