from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..component.car_component import CarComponent
from ..models import Car
from ..utils.serializer.car_serializer import CarSerializer


class CarViewSet(ViewSet):
    """
    this is the Car View that will handle the CRUD operation For the Car Model
    """

    def list(self, request):
        cars = CarComponent.get_cars()

        result = CarSerializer(cars, many=True)

        return Response(data=result.data, status=200)

    def create(self, request):
        request_data = request.data
        car = CarComponent.create_car("car")
        result = CarSerializer(car, many=False)

        return Response(data=result.data, status=201)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

