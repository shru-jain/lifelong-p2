"""
URL configuration for dbquery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from readers.views import index, book_filter, user_filter, users_page, user_alt_filter
from readers.views import  delete_book, delete_user, add_book, add_user, update_book, update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('usersPage/', users_page, name='users_page'),
    path('filter/', book_filter, name='book_filter'),
    path('usersPage/filter/', user_filter, name='user_filter'),
    path('usersPage/altFilter/', user_alt_filter, name='user_alt_filter'),
    path('<int:pk>/delete/', delete_book, name='delete_book'),
    path('usersPage/<int:pk>/delete/', delete_user, name='delete_user'),
    path('addBook/',add_book, name='add_book'),
    path('usersPage/addUser', add_user, name = "add_user"),
    path('update_book/<int:pk>/', update_book, name = "update_book"),
    path('usersPage/update_user/<int:pk>/', update_user, name = "update_user")

]
