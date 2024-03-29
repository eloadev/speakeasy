from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from django.utils.encoding import smart_str

from converter.forms import BookCreate
from converter.helpers.user import is_admin, is_authenticated
from converter.models.book import Book


@user_passes_test(is_authenticated)
@user_passes_test(is_admin)
def create(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/create.html', {'upload_form': upload})


def all(request):
    books = Book.objects.all()
    return render(request, "index.html", books)


@user_passes_test(is_authenticated)
@user_passes_test(is_admin)
def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('index.html')


def retrieve(request, book_id):
    book = Book.objects.get(id=book_id)
    book_file = book.book_file.file
    response = FileResponse(book_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % smart_str(book_file.name)
    return response
