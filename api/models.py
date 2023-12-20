import math

from django.db import models

# Create your models here.
class Plane(models.Model):
    # TODO: Using PositiveSmallIntegerField for id because
    # 1. it needs to be a numeric value inorder to calculate the plane's
    #   fuel tank capacity
    # 2. PositiveSmallIntegerField has a range between 0-32767. This saves
    #   on significant database space compared to usage of similar fields
    #   like BigIntegerField which spans from
    #   (-9223372036854775808 to 9223372036854775807).
    # 3. Using PositiveSmallIntegerField should be more than adequate considering
    #   the largest airline has less than 1000 aircraft. Wikipedia for reference
    #   (https://en.wikipedia.org/wiki/Largest_airlines_in_the_world#Aircraft_owned).
    id = models.PositiveSmallIntegerField(unique=True)
    litres = models.PositiveSmallIntegerField(default=200)
    # TODO: using PositiveSmallIntegerField based on assumption that largest
    # capacity plane is the Airbus A380 (https://en.wikipedia.org/wiki/Airbus_A380)
    # with a capacity of less than 1000.
    # PositiveSmallIntegerField will comfortably accomodate this and leave
    # enough room for future expansion.
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
        return math.log(self.id) * 0.8

    @property
    def passenger_consumption(self):
        """
        Each passenger will impact the plane's fuel consumption (per minute)
        using the formula below.

        passenger_consumption = passengers * 0.002
        """
        return self.passengers * 0.002