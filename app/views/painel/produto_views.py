from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from ...services import produto
from ...models import Estabelecimento, CategoriaProduto, Produto
from ...forms.produto_forms import ProdutoForm


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = "produtos"
    template_name = "painel/produtos/produto_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.estabelecimento = get_object_or_404(Estabelecimento, usuario=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return produto.get_produtos_by_estabelecimento(self.estabelecimento)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_produtos"] = produto.get_total_produtos_by_estabelecimento(self.estabelecimento)
        return context
    

class ProdutoDestaqueListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = "produtos"
    template_name = "painel/produtos/produto_destaque_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.estabelecimento = get_object_or_404(Estabelecimento, usuario=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return produto.get_produtos_destaques_by_estabelecimento(self.estabelecimento)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_produtos"] = produto.get_total_produtos_destaques_by_estabelecimento(self.estabelecimento)
        return context


class ProdutoPromocaoListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = "produtos"
    template_name = "painel/produtos/produto_promocao_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.estabelecimento = get_object_or_404(Estabelecimento, usuario=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return produto.get_produtos_promocao_by_estabelecimento(self.estabelecimento)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_produtos"] = produto.get_total_produtos_promocao_by_estabelecimento(self.estabelecimento)
        return context


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    context_object_name = "produto"
    template_name = "painel/produtos/produto_detail.html"


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "painel/produtos/produto_form.html"
    success_url = reverse_lazy("produtos")
    
    def dispatch(self, request, *args, **kwargs):
        self.estabelecimento = get_object_or_404(Estabelecimento, usuario=request.user)
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        estabelecimento = self.estabelecimento
        kwargs["estabelecimento"] = estabelecimento
        return kwargs
    
    def form_valid(self, form):
        form.instance.estabelecimento = self.estabelecimento
        messages.success(self.request, 'Produto criado com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Novo produto"
        return context


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "painel/produtos/produto_form.html"
    success_url = reverse_lazy("produtos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar produto"
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        estabelecimento = get_object_or_404(Estabelecimento, usuario=self.request.user)
        kwargs["estabelecimento"] = estabelecimento
        return kwargs

    def form_valid(self, form):
        messages.info(self.request, 'Produto editado com sucesso!')
        return super().form_valid(form)


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "painel/produtos/produto_delete.html"
    success_url = reverse_lazy("produtos")

    def form_valid(self, form):
        messages.error(self.request, 'Produto deletado com sucesso!')
        return super().form_valid(form)
