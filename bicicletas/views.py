from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Bicicleta
from .serializers import BicicletaSerializer

class BicicletaViewSet(viewsets.ModelViewSet):
    queryset = Bicicleta.objects.all()
    serializer_class = BicicletaSerializer
    permission_classes = [permissions.IsAuthenticated]
