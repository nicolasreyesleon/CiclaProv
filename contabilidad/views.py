from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import MovimientoContable
from .serializers import MovimientoContableSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum


class MovimientoContableViewSet(viewsets.ModelViewSet):
    queryset = MovimientoContable.objects.all()
    serializer_class = MovimientoContableSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def resumen_contable(request):
    desde = request.query_params.get('desde')
    hasta = request.query_params.get('hasta')

    filtros = {}
    if desde:
        filtros['fecha__gte'] = desde
    if hasta:
        filtros['fecha__lte'] = hasta

    ingresos = MovimientoContable.objects.filter(tipo='ingreso', **filtros).aggregate(total=Sum('monto'))['total'] or 0
    egresos = MovimientoContable.objects.filter(tipo='egreso', **filtros).aggregate(total=Sum('monto'))['total'] or 0
    saldo = ingresos - egresos

    return Response({
        'ingresos': ingresos,
        'egresos': egresos,
        'saldo': saldo,
        'desde': desde,
        'hasta': hasta
    })