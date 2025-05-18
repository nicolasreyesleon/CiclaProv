from django.db import models
from clientes.models import Cliente
from bicicletas.models import Bicicleta

class Reparacion(models.Model):
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default='pendiente')
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE, related_name='reparaciones')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reparaciones')

    def __str__(self):
        return f"{self.tipo} - {self.fecha} ({self.estado})"
