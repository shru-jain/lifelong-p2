from django.shortcuts import render
from .models import User, Book
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .forms import OptionsForm
from django.db.models import Count

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def getForm():
    bookNames = Book.objects.all().values_list('id', 'name')
    choices = [(book[0], book[1]) for book in bookNames]
    form = OptionsForm()
    form.fields['options'].choices = choices
    return form

@csrf_exempt
def index(request):
    
    users = User.objects.all()
    books = Book.objects.all()
    context = {
        'users': users,
        'books': books,
        'form': getForm()
    }
    return render(request, 'booksPage.html', context)



@csrf_exempt
def book_filter(request):
    users = User.objects.all()
    if request.method == 'POST':
        key = str(request.POST.get('key'))
        constraint = str(request.POST.get('constraint'))
        value = str(request.POST.get('value')).strip()
        if key == 'name':
            if constraint == '<':
                books = Book.objects.filter(name__lt=value).order_by('name')
            elif constraint == '>':
                books = Book.objects.filter(name__gt=value).order_by('name')
            else:
                books = Book.objects.filter(name=value).order_by('name')

        else:
            if not is_float(value):
                return render(request, 'booksPage.html', {"users":users})

            if constraint == '<':
                books = Book.objects.filter(price__lt=value).order_by('name')
            elif constraint == '>':
                books = Book.objects.filter(price__gt=value).order_by('name')
            else:
                books = Book.objects.filter(price=value).order_by('name')

    else:
        books = Book.objects.all()
    context = {
        'users': users,
        'books': books,
        'form': getForm()
    }
    return render(request, 'booksPage.html', context)
                
            

@csrf_exempt
def user_filter(request):
    print("herehere")
    books = Book.objects.all()
    if request.method == 'POST':
        key = str(request.POST.get('key'))
        constraint = str(request.POST.get('constraint'))
        value = str(request.POST.get('value')).strip()

        if key == 'userName':
            if constraint == '<':
                users = User.objects.filter(name__lt=value).order_by('name')
            elif constraint == '>':
                users = User.objects.filter(name__gt=value).order_by('name')
            else:
                users = User.objects.filter(name=value).order_by('name')
            
        elif key == 'age':
            if constraint == '<':
                users = User.objects.filter(age__lt=value).order_by('name')
            elif constraint == '>':
                users = User.objects.filter(age__gt=value).order_by('name')
            else:
                users = User.objects.filter(age=value).order_by('name')
        else: #numBooks
            if not is_float(value):
                return render(request, 'booksPage.html', {"books":books})
            if constraint == '<':
                User.objects.annotate(num_liked_books=Count('liked_books')).filter(num_liked_books__lt=value)
            elif constraint == '>':
                User.objects.annotate(num_liked_books=Count('liked_books')).filter(num_liked_books__gt=value)
            else:
                User.objects.annotate(num_liked_books=Count('liked_books')).filter(num_liked_books=value)
    else:
        users = User.objects.all()
    context = {
        'users': users,
        'books': books,
        'form': getForm()
    }
    return render(request, 'booksPage.html', context)



@csrf_exempt
def user_alt_filter(request):
    return index(request)