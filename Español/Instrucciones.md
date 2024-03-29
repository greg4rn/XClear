# PRIMERA PARTE

## ANDROID - TERMUX

Primero necesitamos actualizar en Termux todos los paquetes instalados a las versiones más recientes disponibles.

```bash
pkg upgrade
```
```bash
pkg install android-tools
```
```bash
pkg install python3
```
```bash
pip install tqdm
```
```bash
pkg install wget
```
Seguidamente descargaremos los 2 archivos necesarios `xclear.py` (script) y `exclr.sh` (ejecutable)
```bash
wget https://raw.githubusercontent.com/greg4rn/resources/main/xclear_es.py ; wget https://raw.githubusercontent.com/greg4rn/resources/main/exclr_es.sh
```

### Detalles: 

- Cuando ejecutemos `pkg upgrade` nos aparecerán algunas preguntas, pero solo en la 1era pregunta confirmamos la instalación con una `Y` y luego presionamos `Enter`. Habrá como 6 preguntas más y en estas presionamos únicamente `Enter` para dejarle con la opción por defecto que es `N`.
- `android-tools`: Nos sirve para interactuar con dispositivos Android conectados y ejecutar comandos ADB.
- `python3`: Nos sirve para ejecutar el script de Python.
- `tqdm`: Nos muestra una barra de progreso visual de las operaciones.
- `wget`: Permite descargar archivos desde la web. Sin embargo, puedes utilizar el comando `nano xclear_es.py` para crear nuestro archivo de python, ahí deberás pegar el código que te comparto y no te olvides guardar el archivo antes de salir del editor.

# SEGUNDA PARTE

## Configuración del Terminal Android

1. Definir IP estática en tu terminal Android cuando se conecte a tu red WiFi de confianza.
2. Habilitar el modo `Opciones de programador` u `Opciones de desarrollador`, para cada terminal Android es distinta la opción para activar. Puedes buscar en YouTube “Como activar Opciones de desarrollador “.
3. Conectar terminal Android al PC mediante cable.

## Configuración desde Windows:

1. Descargar e instalar la última version Minimal ADB and Fastboot Tool (all versions)
2. Abrir “Minimal ADB and Fastboot”
3. Ejecutar los siguientes códigos:
    ```bash
    adb kill-server
    ```
    ```bash
    adb tcpip 5555
    ```
    Ahora, en tu terminal Android debe aparecer una ventana que debes permitirle el acceso 2 veces (Puedes marcar la casilla para permitir siempre el acceso desde ese PC, pero no lo recomiendo)

## Configuración desde TERMUX en tu Terminal Android:

1. Desde tu terminal Android ingresa a Termux y ejecuta los siguientes comandos (aquí debes ingresar la IP estática que definiste en tu terminal Android; esta es la IP estática que configuré en mi terminal Android: 192.168.1.50, tu debes reemplazarla con `tú.direccion.ip.estática:5555`).

    ```bash
    adb connect 192.168.1.50:5555
    ```
    ```bash
    adb kill-server
    ```
    ```bash
    adb devices
    ```
2. Nos falta darle permiso de ejecución a nuesto script, para ello ejecutamos el comando
    ```bash
    chmod +x exclr_es.sh
    ```
3.	Finalmente ya podremos ejecutar el comando
    ```bash
    ./exclr_es.sh
    ```
## Para volver a ejecutar el script
1.	Abres Termux y ejecutas lo siguiente:
    ```bash
    ./exclr_es.sh
    ```
2.	De igual manera no te olvides cerrar la ejecución seleccionando la opción 4.
    
    IMPORTANTE: La desventaja es que las Opciones de desarrollador deben mantenerse habilitadas para que funcione el script. En caso de desactivar esta opción, se necesita de un dispositivo externo (como una PC con android-tools) para ejecutar comandos ADB hacia el terminal Android.


## ¿ALGO SALIÓ MAL?
Empecemos de nuevo, restablezcamos todo con esta configuración.
1.	En Opciones de desarrollador seleccionar la opción “Revocar dispositivos” (está debajo de Depuración USB)
2.	Desactivar Depuración de USB
3.	Desactivar Opciones de programador
4.	En la app de Termux ejecutar:
    ```bash
    adb kill-server
    ```
    ```bash
    exit
    ```
5.	Android: Forzar detención de Termux y borrar la caché de esta app.
6.	En Windos abrir “Minimal ADB and Fastboot” y ejecutar: adb kill-server.
7.	¡Empecemos desde SEGUNDA PARTE! (Pero, si borras los datos de Termux, debes empezar desde la PRIMERA PARTE)
