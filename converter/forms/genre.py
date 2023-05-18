from django import forms
from converter.models.genre import Genre


class GenreCreate(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'genre_name',
        ]
