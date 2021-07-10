from django.shortcuts import render, redirect
from .models import Show, Network
from django.contrib import messages

def base(request):
    return redirect('/shows')

def new_show(request):
    return render(request, 'create_show.html')

def create_shows(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    network_post = request.POST['network']
    show1 = Show.objects.create(
        title = request.POST['title'],
        release_date = request.POST['release_date'],
        network = Network.objects.create(name=network_post),
        description = request.POST['description']
    )
    return redirect(f'/shows/{show1.id}')

def single_show(request, id):
    context = {
        'single_show': Show.objects.get(id=id),
        'networks': Network.objects.all()
    }
    return render(request, 'read_show.html', context)

def all_shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def update_show(request, id):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network.name = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.network.save()
    show.save()
    return redirect(f'/shows/{show.id}')

def edit_show(request, id):
    context = {
        'single_show': Show.objects.get(id=id),
        'networks': Network.objects.all()
    }
    return render(request, 'edit_shows.html', context)

def delete_show(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/shows')