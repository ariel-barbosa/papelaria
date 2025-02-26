from django import forms
from app.models import CadastroAutores, CadastroLivros

class LivroForm(forms.ModelForm):

    autores = forms.ModelMultipleChoiceField(queryset=CadastroAutores.objects.all(), widget=forms.CheckboxSelectMultiple, label='Autores')
    
    class Meta:
        model = CadastroLivros
        
        fields = ['isbn', 'edicao', 'editora', 'ano_publicacao', 'preco_capa', 'categoria', 'autores']


class CadastroAutoresForm(forms.ModelForm):
    class Meta:
        model = CadastroAutores
        fields = ['nome_completo', 'nacionalidade', 'biografia', 'cadastro_livros']


