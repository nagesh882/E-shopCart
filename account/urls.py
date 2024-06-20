from django.urls import path
from account import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.sign_in, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signout/', views.sign_out, name='signout'),

]
