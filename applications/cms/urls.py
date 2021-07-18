from django.urls import path

from . import views

app_name = 'docs'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('docs/usuarios/', views.Index.as_view(), name='usuarios'),
    path('docs/bodega/', views.Index.as_view(), name='bodega'),
    path('docs/venta/', views.Index.as_view(), name='venta'),
]