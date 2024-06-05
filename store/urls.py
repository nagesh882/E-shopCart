from django.urls import path
from store import views


urlpatterns = [
    
    path('', views.storePage, name='storePage'),
    path('<slug:category_slug>/', views.storePage, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

]
