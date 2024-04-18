from django.urls import path, include
from . import views

app_name='order'
urlpatterns = [    
    path('order_detail/<int:pk>/', views.order_detail, name='order_detail'), 
    path("cart/<int:pk>", views.cart, name='cart'),
    path("modify_cart/", views.modify_cart, name='modify_cart'),    
    path("add_cart/", views.add_cart, name='add_cart'),    
    path("remove_cart/", views.cart_remove, name='remove_cart'),    
    path("cart_delete/<int:pk>", views.cart_delete, name='delete'),
]
