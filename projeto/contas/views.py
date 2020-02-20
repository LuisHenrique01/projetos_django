# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacoa
from .form import TransacoaForms

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %(now)
    return HttpResponse(html)

def pg1(request):
    base = {}
    base['t'] = Transacoa.objects.all()
    return render(request, 'contas/pg1.html', base)

def cadastrar(request):
    form = TransacoaForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request, 'contas/cadastro.html', {'form': form})

def update(request, pk):
    trasacao = Transacoa.objects.get(pk=pk)
    form = TransacoaForms(request.POST or None, instance=trasacao)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    return render(request, 'contas/cadastro.html', {'form': form, 'transacao': trasacao})


def delete(request, pk):
    transacao = Transacoa.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_home')
