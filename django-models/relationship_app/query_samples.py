from relationship_app import models


def get_books_by_author(author_name):
    
    return models.Book.objects.filter(author__name=author_name)
def list_all_books_in_library(library_name):

    library = models.Library.objects.get(name=library_name)
    return library.books.all()
    
def get_librarian_of_library(library_name):
    librarian=models.Librarian.objects.get(library__name=library_name)
    return librarian.name