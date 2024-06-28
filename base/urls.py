from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby),
    path('lobby/', views.lobby,  name='lobby'),
    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    path('salvar_no_json/', views.salvar_no_json, name='salvar_no_json'),
    path('espera/', views.espera, name='espera'),
    path('listar_pessoas_em_espera/', views.listar_pessoas_em_espera, name='listar_pessoas_em_espera')
    
]