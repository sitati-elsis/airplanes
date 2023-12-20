from api import models


def create_plane_entry(validated_json):
    """
    Helper method to create Phone entries in the database.
    """
    new_plane = models.Plane()
    new_plane.id = validated_json['id']
    new_plane.passengers = validated_json['passengers']
    new_plane.save()

def fetch_planes():
    """
    Helper method to fetch all planes from the database.
    """
    return models.Plane.objects.all()

def calculate_flight_data(planes):
    """
    This method takes in ten plane objects (in the form of a Django queryset)
    and does the following...
        1. Calculates the combined total consumption per minute.
        2. Calculates the maximum number of minutes a plane is able to fly.
        3. Returns a tuple consisting of "total consumption per minute" and
            "maximum minutes able to fly".
    """
    # combined total consumption per minute.
    total_consumption_all_flights = 0
    # NOTE: The most fuel efficient flight will have the least fuel consumption
    # and therefore will also have the ability to fly maximum minutes in a flight.
    most_fuel_efficient = float('inf')
    maximum_minutes = 0
    for plane in planes:
        total_consumption_all_flights += plane.total_fuel_consumption
        if most_fuel_efficient > plane.total_fuel_consumption:
            most_fuel_efficient = plane.total_fuel_consumption
            maximum_minutes = (
                plane.fuel_tank_capacity /
                    plane.total_fuel_consumption
            )
    return total_consumption_all_flights, maximum_minutes