from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'review']
        labels = {
            'title': 'Название:',
            'description': 'Описание:',
            'review': 'Отзыв:',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
