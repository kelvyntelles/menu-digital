from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from ...services import categoria_produto
from ...models import Estabelecimento, CategoriaProduto


class CategoriaListView(LoginRequiredMixin, ListView):
    model = CategoriaProduto
    context_object_name = "categorias"
    template_name = "painel/categorias/categoria_list.html"

    def dispatch(self, request, *args, **kwargs):
        self.estabelecimento = get_object_or_404(Estabelecimento, usuario=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return categoria_produto.get_categorias_by_estabelecimento(self.estabelecimento)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_categorias"] = categoria_produto.get_total_categorias_produto_by_estabelecimento(self.estabelecimento)
        return context


class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = CategoriaProduto
    context_object_name = "categoria"
    template_name = "painel/categorias/categoria_detail.html"
    

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = CategoriaProduto
    fields = ["nome"]
    template_name = "painel/categorias/categoria_form.html"
    success_url = reverse_lazy("categorias")
    
    def form_valid(self, form):
        estabelecimento = get_object_or_404(Estabelecimento, usuario=self.request.user)
        form.instance.estabelecimento = estabelecimento
        messages.success(self.request, 'Categoria criada com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Nova categoria"
        return context
    

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = CategoriaProduto
    fields = ["nome"]
    template_name = "painel/categorias/categoria_form.html"
    success_url = reverse_lazy("categorias")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar categoria"
        return context

    def form_valid(self, form):
        messages.info(self.request, 'Categoria editada com sucesso!')
        return super().form_valid(form)

class CategoriaDeleteView(DeleteView):
    model = CategoriaProduto
    template_name = "painel/categorias/categoria_delete.html"
    success_url = reverse_lazy("categorias")

    def form_valid(self, form):
        messages.error(self.request, 'Categoria deletada com sucesso!')
        return super().form_valid(form)
