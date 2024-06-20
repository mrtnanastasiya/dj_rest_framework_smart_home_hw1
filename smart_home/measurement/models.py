from django.db import models

# Нужно как-то связать отношением сенсоры и измерения
# нам нужно знать какое измерение к какому сенсору относится
# не забываем про related_field
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)






# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
