from django import forms
from .models.book import Book
from .models.genre import Genre


class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_title',
            'book_description',
            'book_author',
            'book_year',
            'book_file',
            'genres',
        ]

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class GenreCreate(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'genre_name',
        ]
