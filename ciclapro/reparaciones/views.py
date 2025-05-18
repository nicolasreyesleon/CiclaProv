from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Reparacion
from .serializers import ReparacionSerializer
from contabilidad.models import MovimientoContable

class ReparacionViewSet(viewsets.ModelViewSet):
    queryset = Reparacion.objects.all()
    serializer_class = ReparacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        reparacion = serializer.save()
        MovimientoContable.objects.create(
            tipo='ingreso',
            descripcion=f"Reparación: {reparacion.tipo} - Cliente: {reparacion.cliente.nombre}",
            monto=reparacion.costo
        )
