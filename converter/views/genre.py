from django.http import HttpResponse
from django.shortcuts import redirect, render

from converter.forms import GenreCreate


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