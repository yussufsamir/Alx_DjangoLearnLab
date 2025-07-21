from django.http import HttpResponse
from django.shortcuts import render
from . models import Author, Book
from django.views.generic.detail import DetailView
from .models import Library
# Create your views here.

def list_books(request):
    books = Book.objects.select_related('author').all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
