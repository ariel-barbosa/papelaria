from django.db import models

class CadastroLivros(models.Model):
    
    isbn = models.CharField(max_length=13)
    edicao = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    ano_publicacao = models.TextField()  
    preco_capa = models.FloatField()
    categoria = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)

class CadastroAutores(models.Model):
    
    nome_completo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)
    biografia = models.CharField(max_length=1000)
    cadastro_livros = models.ForeignKey('CadastroLivros', models.DO_NOTHING)

class ControleEstoque(models.Model):
    
    quantidade_livros = models.IntegerField()
    controle_estoquecol = models.IntegerField()
    data_entrada_livro = models.DateField()
    data_saida_livro = models.DateField()
    cadastro_livros = models.ForeignKey(CadastroLivros, models.DO_NOTHING)