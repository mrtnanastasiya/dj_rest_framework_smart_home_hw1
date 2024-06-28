from django.urls import path
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView

from measurement.views import InfoAddSensorViewSet, SensorViewSet, AddMeasurementViewSet

urlpatterns = [
    path('sensor/', InfoAddSensorViewSet.as_view()),
    path('sensor/<pk>/', SensorViewSet.as_view()),
    path('measurement/', AddMeasurementViewSet.as_view()),
    path('sensors/', InfoAddSensorViewSet.as_view()),

]
