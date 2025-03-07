from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=13, unique=True)  # ISBN-13 standard
    category = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# Borrower Model (Library Users)
class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Book Issue Model (Track Borrowed Books)
class BookIssue(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)

    def is_overdue(self):
        return date.today() > self.due_date and self.returned_date is None

    def __str__(self):
        return f"{self.book.title} issued to {self.borrower.user.username}"

# Fine Model (For Late Returns)
class Fine(models.Model):
    book_issue = models.OneToOneField(BookIssue, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fine of {self.amount} for {self.book_issue.borrower.user.username}"
