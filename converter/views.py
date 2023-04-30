from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str

from .models.book import Book, Genre
from converter.forms import BookCreate, GenreCreate


def index(request):
    books = Book.objects.all
    genres = Genre.objects.all
    context = {
        'books': books,
        'genres': genres,
    }
    return render(request, "index.html", context)


def genre_create(request):
    upload = GenreCreate()
    if request.method == 'POST':
        upload = GenreCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'genre_create.html', {'upload_form': upload})


def book_create(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book_create.html', {'upload_form': upload})


def book_retrieve(request, book_id):
    book = Book.objects.get(id=book_id)
    book_file = book.book_file.file
    response = FileResponse(book_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % smart_str(book_file.name)
    return response
