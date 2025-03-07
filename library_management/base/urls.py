from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('login_student/', views.login_student, name='student'),
    path('available_books/', views.available_books, name='book'),
]
