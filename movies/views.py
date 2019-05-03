from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from movies.forms import FilmeForm
from movies.models import Filme


@login_required
def filme_new(request):
    filme_file = ''

    form = FilmeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('movies:filmes_list')
    context = {'filme_file': filme_file,
               'form': form}

    return render(request, 'movies/novoFilme.html', context)



@login_required
def filmes_list(request):
    # titulo = request.GET.get('titulo', None)
    # ano = request.GET.get('ano', None)

    # if titulo or ano:
    #     filmes = Filme.objects.filter(first_name__icontains=titulo) | Filme.objects.filter(last_name__icontains=ano)
    # else:

    filmes = Filme.objects.all()

    # persons = Person.objects.all()
    return render(request, 'movies/lista_filmes.html', {'filmes': filmes})



@login_required
def filmes_update(request, id):
    filme = get_object_or_404(Filme, pk=id)
    filme_file = filme.videofile

    form = FilmeForm(request.POST or None, request.FILES or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('movies:filmes_list')

    context = {'filme_file': filme_file,
               'form': form}
    return render(request, 'movies/novoFilme.html', context)


@login_required
def filmes_delete(request, id):
    filme = get_object_or_404(Filme, pk=id)
    form = FilmeForm(request.POST or None, request.FILES or None, instance=filme)

    if request.method == 'POST':
        filme.delete()
        return redirect('movies:filmes_list')

    return render(request, 'movies/filme_delete.html', {'filme': filme})



