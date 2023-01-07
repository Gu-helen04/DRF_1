from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, SensorDetail


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class SensorSerializer_all(serializers.ModelSerializer):
    class Meta:
        model = SensorDetail
        fields = ['id', 'name', 'description', 'measurements']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDetail
        fields = ['id', 'name', 'description']
