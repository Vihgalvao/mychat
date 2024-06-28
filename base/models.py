from django.db import models

# Create your models here.

class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Requisicao(models.Model):
    room = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)