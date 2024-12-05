from django.db import models
from django.contrib.auth.models import User  # Modelo de usuários do Django

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Participante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eventos_inscritos = models.ManyToManyField(Evento, related_name="participantes", blank=True)

    def __str__(self):
        return self.user.username
