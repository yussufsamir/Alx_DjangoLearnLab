from django import views
from django.urls import include, path
from .views import list_books, LibraryDetailView
from django.urls import path
from .views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register.as_view(), name="register"),  
]



