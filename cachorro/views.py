from django.shortcuts import render, redirect
from cachorro.models import Cachorro
from cachorro.forms import CachorroForm

# Create your views here.
def home1(request):
    cachorros = Cachorro.objects.filter().all()
    args = {'cachorros':cachorros}
    return render(request, 'home1.html', args)
    

def cadastros2(request):
    form = CachorroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    args = {'form':form}
    return render(request, 'cadastro2.html', args)
def lista_cachorros(request):
    lista_cachorros = Cachorro.objects.filter().all()

    args = {'lista_cachorros':lista_cachorros}
    return render(request, 'listacachorros.html', args)

def detalhes_cachorro(request, id):
    cachorro = Cachorro.objects.get(pk=id)

    args = {'cachorro':cachorro}
    return render(request, 'detalhescao.html', args)

def atualizar_cachorro(request, id):
    cachorro = Cachorro.objects.get(pk=id)
    form = CachorroForm(request.POST or None, instance=cachorro)

    args = {'form':form}

    if form.is_valid():
        form.save()
        args = {
            'msg':'Cadastro atulizado com sucesso'
        }
    return render(request, 'atualizarcao.html', args)

def deletar_cachorro(request, id):
    cachorro = Cachorro.objects.get(pk=id)
    cachorro.delete()

    args = {
        'msg':'O cahorro foi deletado com sucesso',
        'cachorro':cachorro
        }
    return render(request, 'detalhescao.html', args) 