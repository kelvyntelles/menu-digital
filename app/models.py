from django.db import models
from django.contrib.auth.models import User

class UsuarioPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.celular}"


class Estabelecimento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="estabelecimentos/", null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    is_ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class CategoriaProduto(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='categorias')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.estabelecimento.nome}"


class Produto(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='produtos')
    logo = models.ImageField(upload_to="produtos/", null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categorias = models.ManyToManyField(CategoriaProduto, related_name='produtos')
    destaque = models.BooleanField(default=False)
    promocao = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.estabelecimento.nome}"
