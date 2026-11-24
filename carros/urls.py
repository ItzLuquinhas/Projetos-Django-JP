from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('carro/<int:pk>/', views.detalhe, name='detalhe'),
    path('cadastro/', views.cadastro, name='cadastro'),
]