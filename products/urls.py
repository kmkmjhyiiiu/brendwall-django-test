from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('list/', views.get_products, name='get_products'),
    path('', views.index, name='show_product'),
]
