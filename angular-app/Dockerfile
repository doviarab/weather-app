### Primera etapa: construir angular ###

# Se deja referenciado como builder
FROM node:16-alpine

# Se configura directorio
WORKDIR /app

# Se copian dependencias
COPY angular-app/package.json angular-app/package-lock.json /app/

# Se instalan
RUN npm install -g @angular/cli && ls && npm install

# Se copian archivos.
COPY angular-app/. /app

# Se construye app
CMD ["ng","serve","--host", "0.0.0.0", "--disable-host-check"]