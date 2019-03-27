from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from clientes.models import Person
from clientes.forms import PersonForm


@login_required
def persons_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    if nome or sobrenome:
        persons = Person.objects.filter(first_name__icontains=nome) | Person.objects.filter(last_name__icontains=sobrenome)
    else:
        persons = Person.objects.all()

    # persons = Person.objects.all()
    return render(request, 'clientes/person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('clientes:persons_list')
    return render(request, 'clientes/personFormTempl.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('clientes:persons_list')

    return render(request, 'clientes/personFormTempl.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('clientes:persons_list')

    return render(request, 'clientes/personDeleteConfirmTempl.html', {'person': person})
