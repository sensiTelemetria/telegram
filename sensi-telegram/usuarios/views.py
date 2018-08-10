from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuarios.models import usuario
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import usuarioForm


def novo_usuario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'novo_usuario.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = usuarioForm()
    return render(request, 'novo_usuario.html', {'form': form})


def usuarios(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
    usuarios = usuario.objects.all()
    return render(request, 'lista_usuarios', {'usuarios': usuarios})

def deleta_usuario(request, id):
    usuario.objects.get(id=id).delete()
    return redirect('lista_usuarios')
