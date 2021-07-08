from django.shortcuts import render, redirect
from .models import Book, Author

def all_books(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, 'all_books.html', context)

def create_book(request):
    book1 = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['description']
    )
    return redirect('/all_books')

def single_book(request, id):
    context = {
        'single_book': Book.objects.get(id=id),
        'authors': Author.objects.all()
    }
    return render(request, 'book.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'all_authors.html', context)

def create_author(request):
    author1 = Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def single_author(request, id):
    context = {
        'single_author': Author.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request, 'author.html', context)

def add_author(request):
    current_book = Book.objects.get(id=request.POST['book'])
    current_author = Author.objects.get(id=request.POST['author'])
    current_book.authors.add(current_author)
    return redirect(f'/all_books/{current_book.id}')

def add_book(request):
    current_book = Book.objects.get(id=request.POST['book'])
    current_author = Author.objects.get(id=request.POST['author'])
    current_author.books.add(current_book)
    return redirect(f'/authors/{current_author.id}')