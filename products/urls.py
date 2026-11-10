from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<slug:slug_category>/', views.products_list, name='products_list_with_category'),
    path('<int:id>/<slug:slug>/', views.products_detail, name='product_detail')
]