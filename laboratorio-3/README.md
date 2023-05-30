# Laboratorio 1

## Criptografía y Seguridad en Redes

Nicolás Chirino - S1

### Descripción de actividades

Su informante quiere entregar la contraseña de acceso a una red, pero desconfía de todo medio para entregársela (aún no llega al capítulo del curso en donde aprende a comunicar una password sin que nadie más la pueda interceptar).
Por lo tanto, le entregará un archivo que contiene un desafío de autenticación, que al analizarlo, usted podrá obtener la contraseña que lo permite resolver.
Como nadie puede ver a su informante (es informante y debe mantener el anonimato), él se comunicará con usted a través de la redes inalámbricas y de una forma que solo usted, como experto en informática y telecomunicaciones, logrará esclarecer.

- Identifique cual es la red inalámbrica que está utilizando su informante para enviarle información. Obtenga la contraseña de esa red utilizando el ataque por defecto de aircrack-ng, indicando el tiempo requerido para esto. Descifre el contenido transmitido sobre ella y descargue de Internet el archivo que su informante le ha comunicado a través de los paquetes que usted ha descifrado.
- Descargue el diccionario de “rockyou”(utilizado ampliamente en el mundo del pentesting). Haga un script para cada string contenido en el diccionario, reemplace la primera letra por su letra en capital y agregue un cero al final de la password.
- Todos los strings que comiencen con número toca eliminarlos del diccionario. Indique la cantidad de contraseñas que contiene el diccionario modificado debe llamarse “rockyou_mod.dic”. A continuación un ejemplo de cómo se modifican las 10 primeras líneas del diccionario original.

### About

En esta repo se incluirán los códigos utilizados así como los archivos .pcap. Algunos archivos no están presentes en la repo puesto que exceden el tamaño límite de github.

### Paso 1

Obtener la WEP Key con aircrack

```shell
sudo airdecap-ng -a 1 capture-01.cap
```

Descifrar el contenido

```shell
sudo airdecap-ng -w 1234567890 capture-01.cap
```

### Paso 2

Script para modificar diccionario

```shell
python3 modify_strings.py rockyou.txt rockyou_mod.dic
```

Contar número de passwords

```shell
python3 count.py rockyou_mod.dic
```

### Paso 3

Obtener password con hashcat

```shell
hashcat -m 22000 -o output.txt hash.hc22000 rockyou_mod.dic
```

Obtener password con hashcat sin potfile

```shell
hashcat -m 22000 -o output.txt hash.hc22000 rockyou_mod.dic --potfile-disable
```

Obtener password con aircrack

```shell
sudo aircrack-ng -w rockyou_mod.dic handshake.pcap
```
