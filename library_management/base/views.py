from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book
# Create your views here.

def loginpage(request):
   
  if request.method == "POST":

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)
            return redirect('student')
    else:
       return HttpResponse("Invalid login credentials.")
  
  return render(request, 'authenticate/login.html')

def register(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request,'Account was created for ' + user)
    return redirect('login')

  context = {'form':form}
  return render(request, 'authenticate/register.html', context)

def home(request):
  return render(request, 'authenticate/home.html',)

def about(request):
  return render(request, 'authenticate/about.html',)

def login_student(request):
  
  return render(request, 'authenticate/login_student.html',)

def available_books(request):

  books = Book.objects.all()
  context = {'books':books,}
  return render(request, 'authenticate/available_books.html', context)