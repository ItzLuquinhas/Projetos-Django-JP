from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarroForm
from .models import Carro


def lista(request):
    carros = Carro.objects.all()

    q = request.GET.get('q', '').strip()
    marca = request.GET.get('marca', '')
    ordem = request.GET.get('ordem', '')

    if q:
        carros = carros.filter(Q(marca__icontains=q) | Q(modelo__icontains=q))
    if marca:
        carros = carros.filter(marca=marca)

    ordens = {
        'preco_asc': 'preco',
        'preco_desc': '-preco',
        'potencia': '-potencia_cv',
        'velocidade': '-velocidade_max',
    }
    if ordem in ordens:
        carros = carros.order_by(ordens[ordem])

    marcas = Carro.objects.values_list('marca', flat=True).distinct().order_by('marca')

    return render(request, 'lista.html', {
        'carros': carros,
        'marcas': marcas,
        'q': q,
        'marca_sel': marca,
        'ordem_sel': ordem,
    })


@login_required
def detalhe(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    return render(request, 'detalhe.html', {'carro': carro})


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})


# ---------- ANÚNCIOS ----------

def _checar_permissao(user, carro):
    """Só o dono ou um admin mexe no anúncio."""
    if carro.dono != user and not user.is_staff:
        raise PermissionDenied


@login_required
def criar(request):
    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            carro = form.save(commit=False)
            carro.dono = request.user
            carro.save()
            return redirect('detalhe', pk=carro.pk)
    else:
        form = CarroForm()
    return render(request, 'form_carro.html', {'form': form, 'titulo': 'Anunciar um carro'})


@login_required
def editar(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    _checar_permissao(request.user, carro)

    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('detalhe', pk=carro.pk)
    else:
        form = CarroForm(instance=carro)
    return render(request, 'form_carro.html', {'form': form, 'titulo': 'Editar anúncio'})


@login_required
def excluir(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    _checar_permissao(request.user, carro)

    if request.method == 'POST':
        carro.delete()
        return redirect('meus')
    return render(request, 'confirmar_exclusao.html', {'carro': carro})


@login_required
def meus(request):
    carros = Carro.objects.filter(dono=request.user)
    return render(request, 'meus_anuncios.html', {'carros': carros})