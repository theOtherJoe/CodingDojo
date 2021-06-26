from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def display(request):
    context = {
        'fullname': request.POST['name'],
        'dojolocation': request.POST['location'],
        'language': request.POST['fav_language'],
        'finalcomment': request.POST['comment']
    }
    return render(request, 'result.html', context)