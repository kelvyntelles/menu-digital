from django.urls import path
from .views.painel import (
    cliente_views, autenticacao_views, categoria_produto_views, produto_views
)

urlpatterns = [
    # ROTAS DE AUTENTICACAO
    path('login', autenticacao_views.login_view, name='login'),
    path("alterar_senha/", autenticacao_views.AlterarSenhaView.as_view(), name="alterar_senha"),
    path("logout/", autenticacao_views.logout_view, name="logout"),
    
    
    # ROTAS DE CLIENTES
    path('dashboard', cliente_views.dashboard, name='dashboard'),
    path('estabelecimento/<int:pk>', cliente_views.EstabelecimentoDetailView.as_view(), name='estabelecimento'),
    path('estabelecimento/<int:pk>/update', cliente_views.EstabelecimentoUpdateView.as_view(), name='estabelecimento_update'),
    
    # ROTAS DE CATEGORIAS
    path('categorias', categoria_produto_views.CategoriaListView.as_view(), name='categorias'),
    path('categorias/<int:pk>', categoria_produto_views.CategoriaDetailView.as_view(), name='categoria'),
    path('categorias/create', categoria_produto_views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/update', categoria_produto_views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete', categoria_produto_views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    
    # ROTAS DE PRODUTOS
    path('produtos', produto_views.ProdutoListView.as_view(), name='produtos'),
    path('produtos/<int:pk>', produto_views.ProdutoDetailView.as_view(), name='produto'),
    path('produtos/create', produto_views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/update', produto_views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/delete', produto_views.ProdutoDeleteView.as_view(), name='produto_delete'),
    
    path('produtos_destaque', produto_views.ProdutoDestaqueListView.as_view(), name='produtos_destaque'),
    path('produtos_promocao', produto_views.ProdutoPromocaoListView.as_view(), name='produtos_promocao'),
]
