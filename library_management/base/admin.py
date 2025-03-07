from django.contrib import admin
from .models import Author, Book, Borrower, BookIssue, Fine

# Registering Models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(BookIssue)
admin.site.register(Fine)
