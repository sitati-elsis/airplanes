from api import models


def create_plane_entry(validated_json):
    """
    Helper method to create Phone entries in the database.
    """
    new_plane = models.Plane()
    new_plane.id = validated_json['id']
    new_plane.passengers = validated_json['passengers']
    new_plane.save()