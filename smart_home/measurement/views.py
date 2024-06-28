# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer

from rest_framework import generics

#GET, POST
class InfoAddSensorViewSet(generics.ListCreateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

# PATCH
class SensorViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

# POST
class AddMeasurementViewSet(generics.CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()




