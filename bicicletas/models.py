from django.db import models
from clientes.models import Cliente

class Bicicleta(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='activa')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='bicicletas')

    def __str__(self):
        return f"{self.marca} - {self.modelo} ({self.cliente.nombre})"