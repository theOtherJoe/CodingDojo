from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('shows', views.all_shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_shows),
    path('shows/<int:id>', views.single_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:id>/destroy', views.delete_show)
]