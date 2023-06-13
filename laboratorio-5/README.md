# Laboratorio 5

## Criptografía y Seguridad en Redes

Nicolás Chirino - S1

## Descripción de Actividades

Para este último laboratorio, nuestro informante ya sabe que puede establecer un medio seguro sin un intercambio previo de una contraseña, gracias al protocolo diffie-hellman. El problema es que ahora no sabe si confiar en el equipo con el cual establezca comunicación, ya que las credenciales de usuario pueden haber sido divulgadas por algún soplón.

Para el presente laboratorio deberá:

Crear 4 contenedores en Docker, donde cada uno tendrá el siguiente SO:

Ubuntu 14.10, Ubuntu 16.10, Ubuntu 18.10 y Ubuntu 20.10, a los cuales llamaremos C1,C2,C3,C4/S1 respectivamente.

## Crear contenedores

Primero es necesario construir cada uno de los Dockerfiles, para ello dirijase a cada carpeta de este laboratorio y ejecute el comando:

```docker
docker build -t <nombre_imagen> .
```

Posteriormente, se necesitará ejecutar cada uno de las imagenes, para esto utilice el comando:

```docker
docker run -it --rm <nombre_imagen> .
```

## Ejecución

- El primer contenedor a ejecutarse debe ser el servidor (S1 o S2).
- Obtenga la IP del contenedor servidor.
- Ejecute `ssh test@<ip_servidor>` en algún contenedor C1, C2, C3, C4, Incognito.
- Realice los pasos para establecer conexión, con contraseña "test".
- Durante el procedimiento, capture el tráfico generado por el servidor desde su máquina local con Wireshark.
