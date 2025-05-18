from django.db import models
from django.db import models
from clientes.models import Cliente

class Venta(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre} - {self.total}"
