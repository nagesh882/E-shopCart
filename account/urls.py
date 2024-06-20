from django.urls import path
from account import views

urlpatterns = [
    path('signup', views.sign_up, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
