from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from app.forms import CadastroAutoresForm, LivroForm
from app.models import CadastroAutores, CadastroLivros


class IndexView(TemplateView):
    template_name = "index.html"
    
class LivroFormView(CreateView):
    template_name = "cadastro_livros.html"
    model = CadastroLivros
    form_class = LivroForm

class CadastroAutoresView(CreateView):
    model = CadastroAutores
    form_class = CadastroAutoresForm  # Formulário que você já definiu
    template_name = 'cadastro_autores.html'  # Template para exibir o formulário
    success_url = reverse_lazy('home')  # URL para onde o usuário será redirecionado após o cadastro

    
    