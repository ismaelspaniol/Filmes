from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from musicas.forms import MusicaForm
from musicas.models import Musica


@login_required
def musica_new(request):
    musica_file = ''

    form = MusicaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('musicas:musicas_list')
    context = {'musica_file': musica_file,
               'form': form}

    return render(request, 'musicas/nova_musica.html', context)


@login_required
def musicas_list(request):

    musicas = Musica.objects.all()

    return render(request, 'musicas/lista_musicas.html', {'musicas': musicas})



@login_required
def musicas_update(request, id):
    musica = get_object_or_404(Musica, pk=id)
    musica_file = musica.musica_file

    form = MusicaForm(request.POST or None, request.FILES or None, instance=musica)

    if form.is_valid():
        form.save()
        return redirect('musicas:musicas_list')

    context = {'musica_file': musica_file,
               'form': form}
    return render(request, 'musicas/nova_musica.html', context)


@login_required
def musicas_delete(request, id):
    musica = get_object_or_404(Musica, pk=id)
    form = MusicaForm(request.POST or None, request.FILES or None, instance=musica)

    if request.method == 'POST':
        musica.delete()
        return redirect('musicas:musicas_list')

    return render(request, 'musicas/musica_delete.html', {'musica': musica})





