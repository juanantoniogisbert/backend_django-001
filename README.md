# DJANGO BACKEND 

- [Juanan](https://github.com/juanantoniogisbert)
- [Alejandro](https://github.com/ALEJ4NDRO29/)


## Requisitos
- [Docker](https://docs.docker.com/install/)
- [Docker-compose](https://docs.docker.com/compose/install/)

## Instalación
    git clone https://github.com/juanantoniogisbert/backend_django-001.git

    cd vue_frontend-001

    sudo docker-compose up --build

El último comando creará la imagen en docker de la aplicación junto a una imagen de Python 3.7.6 y Postgres 12.1

## Descripción 

Backend en Django utilizado en las siguientes aplicaciónnes desarrolladas en React Redux y Vue.js.

 - https://github.com/ALEJ4NDRO29/react_redux_frontend-001
 - https://github.com/juanantoniogisbert/vue_frontend-001


La aplicación consta de un sistema de login y registro de usuarios junto a sus perfiles. 

Podemos realizar gestión de hoteles en base de datos y los usuarios podrán crear comentarios a cada hotel.

Podemos crear hoteles de forma automática mediante faker con las siguientes instrucciones.

    sudo docker exec -it django bash

    python manage.py shell

    exec(open('dbSeed/dbHotelSeed.py').read())
