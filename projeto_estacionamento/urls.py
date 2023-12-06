from django.contrib import admin
from django.urls import path
from app_estacionamento import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mensalista/<int:pk>', views.mensalista, name='mensalista'),
    ]
