from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
]
