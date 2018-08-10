from django.shortcuts import render
from django.http import HttpResponse
from alarmes.models import alarme


# Create your views here.
from .forms import alarmeForm


def novo_alarme(request):
    if request.method == 'POST':
        form = alarmeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Alarme adicionado com sucesso')
        else:
            print(form.errors)
    else:
        form = alarmeForm()

    return render(request, 'novo_alarme.html', {'form': form})



def alarmes(request):
    alarmes = alarme.objects.all()
    return render(request,'lista_alarmes.html', {'alarmes': alarmes})

