from django.urls import path
from shop import views


urlpatterns=[
    path('index/', views.index, name = "index"),
    path('products/', views.products, name = "product"),
    path('orders/', views.orders, name = "orders"),
    path('users/', views.users, name = "users"),
#    path('user/', views.user, name = "user"),
    path('register/', views.register, name = "register"),
]
