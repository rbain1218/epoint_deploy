from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('sell/', views.sell_product, name='sell'),
    path('product/<int:pk>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('products/', views.product_list, name='product_list'),
    path('info/<slug:slug>/', views.info_page, name='info_page'),
]