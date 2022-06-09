from dataclasses import fields
from django import forms
from .models import Livro
from datetime import date

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['name', 'category', 'book_cover', 'author', 'publication_date', 'pages']
    
    def clean_pages(self):
        pages = self.cleaned_data.get('pages')
        if pages <= 0:
            raise forms.ValidationError("Insira uma quantidade válida de paginas!")
        return pages
    
    def clean_publication_date(self):
        ano1500 = date.fromisoformat('1500-01-01')
        ano2022 = date.fromisoformat('2022-12-31')
        publication_date = self.cleaned_data.get('publication_date')
        publication_dateFinal = date.fromisoformat(str(publication_date))
        if ano1500 <= publication_dateFinal <= ano2022:
            return publication_date
        else:
            raise forms.ValidationError("A data de publicação precisa estar entre 1500 e 2022!")
