from .models import Films
from django.forms import ModelForm, TextInput, Textarea

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'description', 'review']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'title', 'name': 'title', 'placeholder': 'Название фильма'}),
            'description': Textarea(attrs={'class': 'form-control', 'id': 'description', 'name': 'description', 'rows': '3', 'placeholder': 'Краткое описание'}),
            'review': Textarea(attrs={'class': 'form-control', 'id': 'review', 'name': 'review', 'rows': '5', 'placeholder': 'Отзыв'}),
        }