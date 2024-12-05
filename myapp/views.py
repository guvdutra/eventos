from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Participante
from django.contrib.auth.decorators import login_required

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'detalhe_evento.html', {'evento': evento})

@login_required
def inscrever_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    participante, created = Participante.objects.get_or_create(user=request.user)
    participante.eventos_inscritos.add(evento)
    return redirect('lista_eventos')
