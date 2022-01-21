from django.apps import AppConfig
import redis
import os


class WeatherAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_app'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':
            print("Esto se ejecuta al iniciar el servidor")
            redisClient = redis.StrictRedis(host='redis', port=6379, db=0)
            coordinates = "-70.6483,-33.4569"
            redisClient.hset("Cities", "Santiago", coordinates)
            coordinates = "8.55,47.3667"
            redisClient.hset("Cities", "Zurich", coordinates)
            coordinates = "174.7667,-36.8667"
            redisClient.hset("Cities", "Auckland", coordinates)
            coordinates = "151.2073,-33.8679"
            redisClient.hset("Cities", "Sydney", coordinates)
            coordinates = "-0.1257,51.5085"
            redisClient.hset("Cities", "Londres", coordinates)
            coordinates = "-83.5002,32.7504"
            redisClient.hset("Cities", "Georgia", coordinates)
