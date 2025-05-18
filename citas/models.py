from django.db import models
from clientes.models import Cliente

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_servicio = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='pendiente')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='citas')

    def __str__(self):
        return f"{self.tipo_servicio} - {self.fecha} {self.hora}"
