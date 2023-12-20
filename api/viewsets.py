from rest_framework import viewsets, status
from rest_framework.response import Response


from api import serializers, utils



class PlaneViewset(viewsets.ViewSet):
    """
    list:
        Returns `total_airplane_fuel_consumption_per_minute`,
        `maximum_minutes_able_to_fly` and a list of `planes` added.
    create:
        Allow for input of an airplane with user defined `id` and `passenger`
        fields.
    """

    def create(self, request):
        serializer = serializers.PlaneSerializer(data=request.data)
        if serializer.is_valid():
            utils.create_plane_entry(serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        planes = utils.fetch_planes()
        flight_data = utils.calculate_flight_data(planes)
        consumption_all_flights, maximum_minutes_flight = flight_data
        json_resp = {
            "total_airplane_fuel_consumption_per_minute": consumption_all_flights,
            "maximum_minutes_able_to_fly": maximum_minutes_flight,
            "planes": serializers.PlaneSerializer(planes, many=True).data
        }
        return Response(json_resp, status=status.HTTP_200_OK)