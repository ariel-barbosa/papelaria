from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name='home'),
    path("cadastro/livro/", views.LivroFormView.as_view(), name='cadastroLivro'),
    path("cadastro/autores/", views.CadastroAutoresView.as_view(), name='cadastroAutores')
]

