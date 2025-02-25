from django import forms
from app.models import CadastroLivros

class LivroForm(forms.ModelForm):
    
    class Meta:
        model = CadastroLivros
        fields = "__all__"