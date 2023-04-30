from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render

from converter.forms import BookCreate
from converter.models.book import Book


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
