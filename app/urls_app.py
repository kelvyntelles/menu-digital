from django.urls import path
from .views.app import estabelecimento_views

urlpatterns = [
    path('estabelecimento/<int:pk>', estabelecimento_views.estabelecimento_view, name='app_estabelecimento'),
    path('estabelecimento/<int:estabelecimento_id>/produto/<int:produto_id>', estabelecimento_views.produto_detail_view, name='app_produto_detail'),
]
