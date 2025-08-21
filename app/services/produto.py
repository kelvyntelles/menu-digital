from ..models import Produto


def get_total_produtos_by_estabelecimento(estabelecimento):
    total = Produto.objects.filter(estabelecimento=estabelecimento).count()
    return total

def get_total_produtos_destaques_by_estabelecimento(estabelecimento):
    total = Produto.objects.filter(estabelecimento=estabelecimento, destaque=True).count()
    return total

def get_total_produtos_promocao_by_estabelecimento(estabelecimento):
    total = Produto.objects.filter(estabelecimento=estabelecimento, promocao=True).count()
    return total

def get_produtos_by_estabelecimento(estabelecimento):
    produtos = Produto.objects.filter(estabelecimento=estabelecimento).order_by("nome")
    return produtos

def get_produtos_destaques_by_estabelecimento(estabelecimento):
    produtos = Produto.objects.filter(estabelecimento=estabelecimento, destaque=True).order_by("nome")
    return produtos

def get_produtos_promocao_by_estabelecimento(estabelecimento):
    produtos = Produto.objects.filter(estabelecimento=estabelecimento, promocao=True).order_by("nome")
    return produtos
