from django.shortcuts import render, redirect
from gato.models import Gato
from gato.forms import GatoForm

# Create your views here.

def home(request):
    gato = Gato.objects.filter().all()
    args = {'gato':gato}
    return render(request, 'home.html', args)
     

def cadastros(request):
    form = GatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    args = {'form':form}
    return render(request, 'cadastro.html', args)
def atualizar_gato(request, id):
    gato = Gato.objects.get(pk=id)
    form = GatoForm(request.POST or None, instance=gato)

    args = {'form':form}

    if form.is_valid():
        form.save()
        args = {
            'msg':'Cadastro do gato atulizado com sucesso'
        }
    return render(request, 'atualizargato.html', args)

def deletar_gato(request, id):
    gato = Gato.objects.get(pk=id)
    gato.delete()

    args = {
        'msg':'O gato foi deletado com sucesso',
        'gato':gato
        }
    return render(request, 'detalhes.html', args) 
def lista_gatos(request):
    lista_gatos = Gato.objects.filter().all()

    args = {'lista_gatos':lista_gatos}
    return render(request, 'listadegatos.html', args)
 
def detalhes_gato(request, id):
        gato = Gato.objects.get(pk=id)

        args = {'gato':gato}
        return render(request, 'detalhes.html', args)