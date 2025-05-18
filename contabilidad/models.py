from django.db import models
from django.db import models

class MovimientoContable(models.Model):
    TIPO_CHOICES = (
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    )

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - ${self.monto} ({self.fecha})"
