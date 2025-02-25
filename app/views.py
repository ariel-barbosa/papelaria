from django import forms
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from app.forms import LivroForm
from app.models import CadastroLivros


class IndexView(TemplateView):
    template_name = "index.html"
    
class LivroFormView(CreateView):
    template_name = "cadastro_livros.html"
    model = CadastroLivros
    form_class = LivroForm
    