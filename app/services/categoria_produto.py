from ..models import CategoriaProduto


def get_total_categorias_produto_by_estabelecimento(estabelecimento):
    total = CategoriaProduto.objects.filter(estabelecimento=estabelecimento).count()
    return total


def get_categorias_by_estabelecimento(estabelecimento):
    categorias = CategoriaProduto.objects.filter(estabelecimento=estabelecimento).order_by("nome")
    return categorias
