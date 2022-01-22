from django.urls import path

from . import views

app_name = 'docs'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('docs/<section>/', views.Index.as_view(), name='index'),
]
