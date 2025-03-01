from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'required': 'required'}),
            'author': forms.TextInput(attrs={'required': 'required'}),
            'publication_year': forms.NumberInput(attrs={'required': 'required'}),
        }
