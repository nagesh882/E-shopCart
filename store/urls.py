from django.urls import path
from store import views


urlpatterns = [
    
    path('', views.storePage, name="storePage"),

]
