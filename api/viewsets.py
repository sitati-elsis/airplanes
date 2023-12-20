from rest_framework import viewsets, status
from rest_framework.response import Response


from api import serializers, utils



class PlaneViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.PlaneSerializer(data=request.data)
        if serializer.is_valid():
            utils.create_plane_entry(serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = models.Plane.objects.all()
        serializer = serializers.PlaneSerializer(queryset, many=True)
        return Response(serializer.data)