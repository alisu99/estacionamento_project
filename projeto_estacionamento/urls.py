from django.contrib import admin
from django.urls import path
from app_estacionamento import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mensalista/<int:pk>', views.mensalista, name='mensalista'),
    path('cadastrar_mensalista', views.cadastrar_mensalista, name='cadastrar_mensalista'),
    path('order_by_vencimento', views.order_by_vencimento, name='order_by_vencimento'),
    path('excluir/<int:pk>', views.excluir, name='excluir'),
    path('atualizar_mensalista/<int:pk>', views.atualizar_mensalista, name='atualizar_mensalista'),
    path('login/', views.login, name='login'),
    path('usuario/', views.usuario, name='usuario')
    ]
