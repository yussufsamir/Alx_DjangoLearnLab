from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from advanced_features_and_security.LibraryProject.bookshelf.models import CustomUserManager

from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse



content_type = ContentType.objects.get_for_model(CustomUserManager)
editors_group, created = Group.objects.get_or_create(name='Editors')
edit_permission = Permission.objects.get(codename='can_edit', content_type=content_type)
create_permission = Permission.objects.get(codename='can_create', content_type=content_type)
editors_group.permissions.add(edit_permission, create_permission)


def delete_article(request, pk):
    if request.user.has_perm('yourapp.can_delete'):
        article = get_object_or_404(CustomUserManager, pk=pk)
        article.delete()
        return HttpResponseRedirect(reverse('article_list'))  # Redirect after deletion
    else:
        return HttpResponseForbidden("You don't have permission to delete this article.")
