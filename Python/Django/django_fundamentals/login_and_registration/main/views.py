from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def home(request):
    return render(request, "reg_login.html")

def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    passwd_hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user1 = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        user_name = request.POST['user_name'],
        email = request.POST['email'],
        password = passwd_hashed
    )
    request.session['log_user_id'] = user1.id
    return redirect('/dash')

def login(request):
    list_of_users = User.objects.filter(user_name=request.POST['user_name'])
    if list_of_users:
        user_logged = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user_logged.password.encode()):
            request.session['log_user_id'] = user_logged.id
            return redirect('/dash')
        else:
            messages.error(request, "Invalid username or password, try again")
            return redirect('/')
    messages.error(request, "Username does not exist")
    return redirect('/')

def dash(request):
    context = {
        'user': User.objects.get(id=request.session['log_user_id'])
    }
    return render(request, "dash.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')