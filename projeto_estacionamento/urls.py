from django.contrib import admin
from django.urls import path
from app_estacionamento import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mensalista/<int:pk>', views.mensalista, name='mensalista'),
    path('cadastrar_mensalista', views.cadastrar_mensalista, name='cadastrar_mensalista'),
    path('order_by_vencimento', views.order_by_vencimento, name='order_by_vencimento'),
    path('excluir', views.excluir, name='excluir')
]
