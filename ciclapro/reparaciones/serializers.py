from rest_framework import serializers
from .models import Reparacion


class ReparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparacion
        fields = '__all__'
