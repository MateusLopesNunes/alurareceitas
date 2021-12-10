from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('cria_receita/', views.cria_receita, name='cria_receita'),
    path('deleta_receita/<int:id>', views.deleta_receita, name='deleta_receita'),
    path('edita_receita/<int:id>', views.edita_receita, name='edita_receita'),
    path('atualiza_receita/', views.atualiza_receita, name='atualiza_receita')
]