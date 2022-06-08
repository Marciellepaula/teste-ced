from dataclasses import fields
from django import forms 
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['name', 'category', 'book_cover', 'author', 'publication_date', 'pages']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        livro = Livro.objects.filter(name=name).count()
        if livro:
            raise forms.ValidationError("Já existe um livro cadastrado com esse nome!")
        return name

    def clean_pages(self):
        pages = self.cleaned_data.get('pages')
        if pages <= 0:
            raise forms.ValidationError("Insira uma quantidade válida de paginas!")
        return pages
    

        
    