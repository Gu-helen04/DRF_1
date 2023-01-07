# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView

from measurement.models import SensorDetail, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorSerializer_all


class SensorInfoView(ListAPIView):
    queryset = SensorDetail.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = SensorDetail.objects.all()
    serializer_class = SensorSerializer_all
