from django.db.models.query import QuerySet


from api import models
from api.typed_json import planes as planes_json


def create_plane_entry(validated_json: planes_json.PlaneDict) -> None:
    """
    Helper method to create Phone entries in the database.
    """
    new_plane = models.Plane()
    new_plane.id = validated_json['id']
    new_plane.passengers = validated_json['passengers']
    new_plane.save()

def fetch_planes() -> QuerySet[models.Plane]:
    """
    Helper method to fetch all planes from the database.
    """
    return models.Plane.objects.all()

def calculate_flight_data(planes:  QuerySet[models.Plane]) -> tuple[float, float]:
    """
    This method takes in ten plane objects (in the form of a Django queryset)
    and does the following...
        1. Calculates the combined total consumption per minute.
        2. Calculates the maximum number of minutes a plane is able to fly.
        3. Returns a tuple consisting of "total consumption per minute" and
            "maximum minutes able to fly".
    """
    # combined total consumption per minute.
    total_consumption_all_flights = 0.0
    # NOTE: The most fuel efficient flight will have the maximum minutes flight
    # duration.
    maximum_flight_minutes = float('inf') * -1
    for plane in planes:
        total_consumption_all_flights += plane.total_fuel_consumption
        current_flight_minutes = plane.fuel_tank_capacity / plane.total_fuel_consumption
        if current_flight_minutes > maximum_flight_minutes:
            maximum_flight_minutes = current_flight_minutes
    return total_consumption_all_flights, maximum_flight_minutes