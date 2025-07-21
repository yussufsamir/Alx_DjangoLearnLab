from django.http import HttpResponse
from django.shortcuts import render
from . models import Author, Book
# Create your views here.

def list_books(request):
    books = Book.objects.select_related('author').all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")

