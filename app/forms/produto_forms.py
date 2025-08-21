from django import forms
from ..models import Produto, CategoriaProduto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ["estabelecimento"]
        labels = {
            "logo": "Imagem",
            "nome": "Nome",
            "descricao": "Descrição",
            "preco": "Preço",
            "categorias": "Categorias",
            "destaque": "Destaque",
            "promocao": "Promoção",
        }

    def __init__(self, *args, **kwargs):
        estabelecimento = kwargs.pop("estabelecimento", None)
        super().__init__(*args, **kwargs)
        if estabelecimento:
            self.fields["categorias"].queryset = CategoriaProduto.objects.filter(
                estabelecimento=estabelecimento
            )