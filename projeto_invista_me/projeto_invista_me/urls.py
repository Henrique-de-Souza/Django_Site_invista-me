from django.contrib import admin
from django.urls import path
from invista_me import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.investimentos, name='investimentos'),
    path('novo_investimento/', views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', views.exluir, name='excluir'),
    path('/<int:id_investimento>', views.detalhe, name='detalhe')

]
