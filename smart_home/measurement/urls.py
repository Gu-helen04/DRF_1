from django.urls import path
from measurement.views import SensorView, MeasurementView, SensorInfoView

urlpatterns = [
    path('sensors/', SensorInfoView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
