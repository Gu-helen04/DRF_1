from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class SensorDetail(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class Measurement(models.Model):
    temperature = models.FloatField()
    sensor = models.ForeignKey(SensorDetail, on_delete=models.CASCADE, related_name='measurements')
    image = models.ImageField(null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
