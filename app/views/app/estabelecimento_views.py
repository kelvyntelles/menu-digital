from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from ...models import Estabelecimento, Produto
from ...services import categoria_produto, produto


def estabelecimento_view(request, pk):
    estabelecimento = get_object_or_404(Estabelecimento, id=pk)
    categorias = categoria_produto.get_categorias_by_estabelecimento(estabelecimento)
    produtos_destaque = produto.get_produtos_destaques_by_estabelecimento(estabelecimento)
    produtos_promocao = produto.get_produtos_promocao_by_estabelecimento(estabelecimento)
    
    return render(request, 'app/estabelecimento.html', {
        "estabelecimento": estabelecimento,
        "categorias": categorias,
        "produtos_destaque": produtos_destaque,
        "produtos_promocao":produtos_promocao
    })


def produto_detail_view(request, estabelecimento_id, produto_id):
    estabelecimento = get_object_or_404(Estabelecimento, id=estabelecimento_id)
    produto = get_object_or_404(Produto, id=produto_id)
    
    return render(request, 'app/produto_detail.html', {
        "estabelecimento": estabelecimento,
        "produto": produto
    })
