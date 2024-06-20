from django.urls import path
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from measurement.views import AddSensorViewSet, AddMeasurementViewSet, ListSensorsViewSet, \
    SensorViewSet

urlpatterns = [
    path('sensor/', AddSensorViewSet.as_view()),
    path('sensor/<pk>/', SensorViewSet.as_view()),
    path('measurement/', AddMeasurementViewSet.as_view()),
    path('sensors/', ListSensorsViewSet.as_view()),

]
