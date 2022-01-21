from channels.consumer import SyncConsumer
import random
import redis
import time
import json
from django.conf import settings
import requests
from weather_app.error import APIError

class WeatherConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        failed = True
        redisClient = redis.StrictRedis(host='redis', port=6379, db=0)
        while (failed):
            try:
                if (random.randint(0,9) < 1):
                    raise APIError("How unfortunate! The API request failed")
                else:
                    failed = False
            except APIError as e:
                timestamp = time.time()
                redisClient.hset("api.errors", timestamp, e.message)

        weathers = {}
        for city in redisClient.hkeys("Cities"):
            cityName = city.decode("utf-8")
            coordinates = redisClient.hget("Cities", cityName).decode("utf-8").split(",")
            url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(coordinates[1], coordinates[0], settings.API_KEY)
            res = requests.get(url)
            data = res.json()
            weathers[data['name']] = data['main']['temp']
            print(json.dumps(weathers))
        self.send({
            "type": "websocket.send",
            "text": json.dumps(weathers),
        })