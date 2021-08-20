from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_reg),
    path('user/register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('create_order', views.create_order),
    path('submit_order', views.submit_order),
    # path('user/update/<int:wish_id>', views.update_wish),
    # path('user/edit/<int:wish_id>', views.edit_wish),
    # path('user/<int:wish_id>/granted', views.grant_wish),
    path('<int:user_id>/<int:ic_id>/like_flavor', views.like_flavor),
    path('<int:user_id>/<int:ic_id>/unlike_flavor', views.unlike_flavor),
    path('orders/<int:order_id>/cancel_order', views.cancel_order),
    path('dashboard', views.user_and_orders),
    path('flavors', views.flavors),
    path('home', views.home),
]