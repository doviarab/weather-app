from django.urls import re_path

from . import weather

websocket_urlpatterns = [
    re_path(r'ws/weather/$', weather.WeatherConsumer.as_asgi()),
]