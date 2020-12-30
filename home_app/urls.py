from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('checkout/', views.checkout,name='checkout'),
    path('menu/', views.menu,name='menu'),
    path('checkout/track_order/', views.track_order,name='checkout/track_order'),
    path('accounts/profile/', views.index,name='index'),
]

