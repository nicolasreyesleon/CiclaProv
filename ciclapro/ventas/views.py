from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Venta
from .serializers import VentaSerializer
from contabilidad.models import MovimientoContable

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        venta = serializer.save()
        MovimientoContable.objects.create(
            tipo='ingreso',
            descripcion=f"Venta #{venta.id} - Cliente: {venta.cliente.nombre}",
            monto=venta.total
        )