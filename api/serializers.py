from rest_framework import serializers

from api import models


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plane
        fields = (
            'id',
            'litres',
            'passengers',
            'fuel_tank_capacity',
            'plane_fuel_comsumption',
            'passenger_consumption',
            'total_fuel_consumption',
        )
        read_only_fields = (
            'litres',
            'fuel_tank_capacity',
            'plane_fuel_comsumption',
            'passenger_consumption',
            'total_fuel_consumption',
        )