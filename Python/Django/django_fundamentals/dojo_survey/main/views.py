from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def createInfo(request):
    request.session['fullname'] = request.POST['name'],
    request.session['dojolocation'] = request.POST['location'],
    request.session['language'] = request.POST['fav_language'],
    request.session['finalcomment'] = request.POST['comment']
    return redirect('/result')

def display(request):
    context = {
        'name': request.session.str(['fullname']),
        'location': request.session['dojolocation'],
        'language': request.session['language'],
        'comment': request.session['finalcomment']
    }
    return render(request, 'result.html', context)