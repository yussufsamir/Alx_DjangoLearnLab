from django.urls import path
from django.contrib.auth import views as auth_views

from django_blog.blog import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="templates/blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="templates/blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
