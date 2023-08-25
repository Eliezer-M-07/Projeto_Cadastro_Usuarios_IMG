from django.urls import path
from app_cadastro_users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listagem/', views.listagem, name='listagem'),
    path('salvar/', views.salvar, name='salvar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar')
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


