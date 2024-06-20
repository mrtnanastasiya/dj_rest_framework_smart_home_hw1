# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorShortDetailSerializer

from rest_framework import generics


# Эндпоинт для добавления сенсора, т.к
# CreateAPIView позволяет только создавать объекты
# методом POST
class AddSensorViewSet(generics.CreateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

# Эндпоинт для взаимодействия с конкретным сенсором
# RetrieveUpdateAPIView позволяет получить объект
# методом GET, или обновить его данные методом PUT/PATCH
class GetSensorViewSet(generics.RetrieveAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

class SensorViewSet(generics.RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

# POST
class AddMeasurementViewSet(generics.CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

# ListAPIView выдает список объектов методом GET
class ListSensorsViewSet(generics.ListAPIView):
    serializer_class = SensorShortDetailSerializer
    queryset = Sensor.objects.all()


