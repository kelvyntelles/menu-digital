from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from ...models import Estabelecimento
from ...services import categoria_produto, produto


@login_required
def dashboard(request):
    estabelecimento = get_object_or_404(Estabelecimento, usuario=request.user)
    total_categorias_produtos = categoria_produto.get_total_categorias_produto_by_estabelecimento(estabelecimento)
    total_produtos = produto.get_total_produtos_by_estabelecimento(estabelecimento)
    total_produtos_destaques = produto.get_total_produtos_destaques_by_estabelecimento(estabelecimento)
    total_produtos_promocao = produto.get_total_produtos_promocao_by_estabelecimento(estabelecimento)
    
    return render(request, 'painel/clientes/dashboard.html', {
        "total_categorias_produtos": total_categorias_produtos,
        "total_produtos": total_produtos,
        "total_produtos_destaques": total_produtos_destaques,
        "total_produtos_promocao": total_produtos_promocao
    })


class EstabelecimentoDetailView(LoginRequiredMixin, DetailView):
    model = Estabelecimento
    context_object_name = "estabelecimento"
    template_name = "painel/clientes/estabelecimento_detail.html"


class EstabelecimentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Estabelecimento
    fields = ["logo", "nome", "descricao"]
    template_name = "painel/clientes/estabelecimento_form.html"

    def get_success_url(self):
        return reverse("estabelecimento", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar estabelecimento"
        return context

    def form_valid(self, form):
        messages.info(self.request, 'Estabelecimento editado com sucesso!')
        return super().form_valid(form)
