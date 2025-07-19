from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year')

admin.site.register(Book,BookAdmin)

