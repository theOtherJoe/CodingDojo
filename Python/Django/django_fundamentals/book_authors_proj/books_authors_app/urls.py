from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books),
    path('create_book', views.create_book),
    path('all_books/<int:id>', views.single_book),
    path('authors', views.authors),
    path('create_author', views.create_author),
    path('authors/<int:id>', views.single_author),
    path('all_books/add_author', views.add_author),
    path('authors/add_book', views.add_book)
]
