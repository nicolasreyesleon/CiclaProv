from rest_framework import serializers
from .models import MovimientoContable

class MovimientoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoContable
        fields = '__all__'
