from django.shortcuts import redirect, render
from .models import Livro
from .forms import LivroForm

# Create your views here.

def listarLivros(request):
    livros = Livro.objects.all()
    return render(request, 'listar-livros.html', {'livros': livros})

def inserirLivro(request):
    form = LivroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar-livros')
    return render(request, 'criar-livro.html', {'form': form})

def atualizarLivro(request, id):
    livro = Livro.objects.get(id=id)
    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('listar-livros')
    return render(request, 'editar-livro.html', {'form': form, 'livro': livro})

def deletarLivro(request, id):
    livro = Livro.objects.get(id=id)
    if request.method == 'POST':
        livro.delete()
    return redirect('listar-livros')
