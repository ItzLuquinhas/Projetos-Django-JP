from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('carro/<int:pk>/', views.detalhe, name='detalhe'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path('anunciar/', views.criar, name='criar'),
    path('carro/<int:pk>/editar/', views.editar, name='editar'),
    path('carro/<int:pk>/excluir/', views.excluir, name='excluir'),
    path('meus-anuncios/', views.meus, name='meus'),
]