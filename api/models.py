import math

from django.db import models

# Create your models here.
class Plane(models.Model):
    id = models.PositiveSmallIntegerField(unique=True)
    # NOTE: Django assigns fields with the name `id` as primary keys by default.
    # To use a field name other than `id` as primary key, define your custom
    # field name and include `primary_key=True`
    plane_id = models.SmallAutoField(primary_key=True)
    litres = models.PositiveSmallIntegerField(default=200)
    passengers = models.PositiveSmallIntegerField()

    @property
    def fuel_tank_capacity(self):
        """
        Fuel tank capacity is calculated using the formula below.

        fuel_tank_capacity = litres * id
        """
        return self.id * self.litres

    @property
    def plane_fuel_comsumption(self):
        """
        Fuel consumption (per minute) when the plane is in flight, regardless
        of whether it contains passengers.

        The formula is calculated as follows.

        plane_fuel_consumption = math.log(id) * 0.8 litres
        """
        # NOTE: Assumption made here is that we are using base10 for logarithms.
        return math.log(self.id, 10) * 0.8

    @property
    def passenger_consumption(self):
        """
        Each passenger will impact the plane's fuel consumption (per minute)
        using the formula below.

        passenger_consumption = passengers * 0.002
        """
        return self.passengers * 0.002

    @property
    def total_fuel_consumption(self):
        """
        This accounts for combined consumption figures (per minute) as shown by
        the formula below.

        total_fuel_consumption =  plane_fuel_comsumption() + passenger_consumption
        """
        return self.plane_fuel_comsumption + self.passenger_consumption