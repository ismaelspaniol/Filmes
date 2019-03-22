from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ferias.models import Ferias


@login_required
def listagem(request):
    ferias = Ferias.objects.all()
    return render(request, 'ferias/listferias.html', {'ferias': ferias})
