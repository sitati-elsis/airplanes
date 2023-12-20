from rest_framework import viewsets
from rest_framework.response import Response


from api import models
from api import serializers


class PlaneViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = models.Plane.objects.all()
        serializer = serializers.PlaneSerializer(queryset, many=True)
        return Response(serializer.data)