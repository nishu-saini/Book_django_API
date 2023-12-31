from django.contrib import admin
from django.urls import path
from book_api.views import BookList, CreateBook, BookInfo

urlpatterns = [
    path('list/', BookList.as_view()),
    path('create-book/', CreateBook.as_view()),
    path('book/<int:pk>/', BookInfo.as_view())
]
