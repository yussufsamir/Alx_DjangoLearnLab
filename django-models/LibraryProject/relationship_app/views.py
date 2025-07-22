from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from . models import Author, Book
from django.views.generic.detail import DetailView
from .models import Library
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
class LoginView(LoginView):
    template_name = "relationship_app/login.html"

class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"