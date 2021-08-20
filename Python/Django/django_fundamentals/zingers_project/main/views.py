from django.shortcuts import render, redirect
from .models import User, Order, IceCream
from django.contrib import messages
import bcrypt
from datetime import datetime, date

def log_reg(request):
    return render(request, "login_reg.html")

def register(request):
    if request.method == 'POST':
        user_errors = User.objects.user_validator(request.POST)
        if len(user_errors) > 0:
            for key, value in user_errors.items():
                messages.error(request, value)
            return redirect('/')

        hashed_passwd = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user1 = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            birthday = request.POST['birthday'],
            password = hashed_passwd
        )
        request.session['current_user'] = user1.id
        return redirect('/dashboard')

def login(request):
    if request.method == 'POST':
        list_of_users = User.objects.filter(email=request.POST['email'])
        if list_of_users:
            user_logged = list_of_users[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user_logged.password.encode()):
                request.session['current_user'] = user_logged.id
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid username or password, try again")
                return redirect('/')
        messages.error(request, "Username does not exist")
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def user_and_orders(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['current_user']),
        'all_orders': Order.objects.all(),
        'all_flavors': IceCream.objects.all()
    }
    return render(request, "dashboard.html", context)

def create_order(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['current_user']),
        'all_orders': Order.objects.all(),
    }
    return render(request, "create_order.html", context)

def submit_order(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('/dashboard')
        user = User.objects.get(id=request.session['current_user'])
        order_errors = Order.objects.order_validator(request.POST)
        if len(order_errors) > 0:
            for key, value in order_errors.items():
                messages.error(request, value)
            return redirect('/create_order')
        if "submit" in request.POST:
            order_created = Order.objects.create(type_of_event = request.POST['type_of_event'], num_of_people = request.POST['num_of_people'], flavor = request.POST['flavor'], cb_selection = request.POST['cb_selection'], orderer = user, special_requests = request.POST['special_requests'])
            return redirect('/dashboard')

def home(request):
    context = {
        'current_user': User.objects.get(id=request.session['current_user']),
        'all_orders': Order.objects.all(),
    }
    return render(request, "home.html", context)

def flavors(request):
    context = {
        'current_user': User.objects.get(id=request.session['current_user']),
        'all_flavors': IceCream.objects.all(),
    }
    return render(request, "flavors.html", context)

def like_flavor(request, user_id, ic_id):
    current_user = request.session['current_user']
    flavor_to_like = IceCream.objects.get(id=ic_id)
    flavor_to_like.users_who_like.add(current_user)
    return redirect('/flavors')

def unlike_flavor(request, user_id, ic_id):
    current_user = request.session['current_user']
    flavor_to_unlike = IceCream.objects.get(id=ic_id)
    flavor_to_unlike.users_who_like.remove(current_user)
    return redirect('/dashboard')

def cancel_order(request, order_id):
    current_user = User.objects.get(id=request.session['current_user'])
    order = current_user.orders.get(id=order_id)
    order.delete()
    return redirect('/dashboard')