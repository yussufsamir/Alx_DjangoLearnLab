from django.shortcuts import redirect, render 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django_blog.blog.forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("home")  
    else:
        form = CustomUserCreationForm()
    return render(request, "templates/blog/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        update_form=UserUpdateForm(request.POST, instance=request.user)
        profile_update=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() and profile_update.is_valid():
            update_form.save()
            profile_update.save()
            return redirect("profile")
        else:
            update_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': update_form, 'p_form': profile_form}
    return render(request, 'templates/blog/profile.html', context)
