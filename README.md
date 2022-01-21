# weather-app
Aplicación de prueba con websockets utilizando django, redis, y angular.
## PREREQUISITOS
Docker >= `20.10`
## PASOS A SEGUIR
Para su utilización, basta ejecutar los siguientes los siguientes comandos en consola:
```shell
docker-compose build
docker-compose up -d
```
Y posteriormente, se podrá acceder a la aplicación ingresando a `localhost:4200` en su navegador.
## CONSIDERACIONES
Asegúrese de tener el archivo `.env.dev` en la raíz del proyecto para tener las variables de entorno requeridas para la ejecución del backend. Este archivo está compuesto de lo siguiente:
```shell
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
API_KEY=*su_api_key*
```
La API_KEY utilizada no viene incluida en el repositorio, pero se puede obtener desde https://openweathermap.org/api creando una cuenta.
