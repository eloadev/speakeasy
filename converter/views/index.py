from django.shortcuts import render, redirect
from converter.models.book import Book, Genre
from converter.tasks import add

# eu te amo <3


def index(request):
    books = Book.objects.all
    genres = Genre.objects.all
    context = {
        'books': books,
        'genres': genres,
    }

    return render(request, "index.html", context)
