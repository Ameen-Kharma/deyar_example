from django.contrib import admin
from django.urls import path, include


from rest_framework import routers

from .views.car_controller import CarViewSet

router = routers.SimpleRouter()

router.register(r'cars', CarViewSet, basename="deyar_cars")

urlpatterns = router.urls



