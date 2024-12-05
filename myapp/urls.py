from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('inscrever/<int:evento_id>/', views.inscrever_evento, name='inscrever_evento'),
]
