# • XClear Android Apps •

## Índice

1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Configuración por PRIMERA VEZ](#configuración-por-primera-vez)
4. [Iniciar](#iniciar)
5. [Exclusión](#exclusión)
6. [Contribuciones](#contribuciones)

## English version 
Visit the next link: [Resources](https://github.com/greg4rn/XClear)

## Introducción
Los script `exclr_es.sh` y `xclear_es.py` permite proporcionar una interfaz para gestionar el funcionamiento y permisos de las aplicaciones en dispositivos Android utilizando comandos ADB (Android Debug Bridge). Estos scripts permitirán forzar la detención y restablecer permisos en todas las aplicaciones del usuario y del sistema.

**¡ADVERTENCIA!**
El mal uso de estas funciones puede causar conflicto en el funcionamiento normal de las aplicaciones y del sistema. Utiliza este código con responsabilidad. No nos hacemos responsables por cualquier inconveniente derivado de su uso indebido.

## Requisitos Previos
Antes de ejecutar el script, asegúrate de tener instaladas las últimas versiones de las siguientes herramientas:

### Paso 1. En Windows
Instalar [Minimal ADB and Fastboot Tool](https://androidmtk.com/download-minimal-adb-fastboot-tool); puedes descargarlo desde su página oficial.

### Paso 2. En Android
**[2.1.]** Descargar e instalar el archivo APK de [Termux](https://termux.dev/), desde su repositorio oficial de [Github](https://github.com/termux/termux-app/releases) o [F-Droid](https://f-droid.org/en/packages/com.termux/).
*NOTA: La versión de Google Play no es compatible.*

**[2.2.]** Configuración en Android
1. Definir IP estática en Android cuando se conecte a la red WiFi de confianza.

**[2.3.]** Activar las Opciones de desarrollador y la Depuración USB en Android.
* Pasos generales:
    1. Ir a Configuración de Android.
    2. Buscar la opción `Acerca del teléfono` y tocar varias veces la opción `Número de compilación` hasta que aparezca el mensaje similar a `¡Ya eres Desarrollador!`.
    3. En la pantalla principal de Configuración se habrá habilitado `Opciones de Desarrollador`, entra ahí y activa `Depuración USB`.
**Nota:** Por razones de seguridad se recomienda desactivar las `Opciones de desarrollador` después de ejecutar el script, sin embargo, deberás volver a conectarte a un PC para volver a utilizar el script.

### Paso 3. En Termux
En Android abrimos la app instalada de Termux y ejecutamos los siguientes comandos, donde confirmamos con una `Y` la instalación de las herramientas y con un `Enter` para dejar la configuración por defecto en el caso de las preguntas de `pkg upgrade`.
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
### 4. Descargar los scripts
Descargar los archivos `exclr_es.sh` y `xclear_es.py`:
```bash
wget httpshttps://raw.githubusercontent.com/greg4rn/resources/main/Espa%C3%B1ol/exclr_es.sh ; wget https://raw.githubusercontent.com/greg4rn/resources/main/Espa%C3%B1ol/xclear_es.py
```
**IMPORTANTE:** Dar permisos de ejecución al script bash
```bash
chmod +x exclr_es.sh
```
### EXPLICACIÓN
- `Minimal ADB and Fastboot Tool`: es una herramienta para Windows, que permite ejecutar comandos ADB desde la consola de Windows hacia un dispositivo Android conectado por cable o Wi-Fi.
- `Termux`: Es un emulador de terminal para Android que permite ejecutar un entorno Linux en un dispositivo Android.
- Cuando se ejecuta `pkg upgrade`, aparecen algunas preguntas, pero solo en la primera pregunta se confirma la actualización con una `Y`. Habrá aproximadamente 5 preguntas o más, donde en esas preguntas se presiona únicamente la tecla `Enter` para dejarle  la opción por defecto que es `N`.
- `android-tools`: Permite interactuar mediante consola y comandos ADB, dentro del entorno de Termux y el dispositivo Android conectado por cable o Wi-Fi.
- `python3`: Permite ejecutar el script de Python.
- `tqdm`: Sirve para visualizar la barra de progreso del script `xclear_es.py`.
- `wget`: Permite descargar archivos desde la web.
- Script Bash `exclr_es.sh`: Permite reducir las líneas de comando a solo la línea de ejecución de este script.
- Script Python `xclear_es.py`: Permite la funcionalidad principal de este proyecto.

## Configuración por PRIMERA VEZ
### En Windows
1. Abrir `Minimal ADB and Fastboot`
2. Ejecutar los siguientes códigos:
    ```bash
    adb kill-server
    ```
    ```bash
    adb tcpip 5555
    ```
    En tu terminal Android debe aparecer una ventana que debes permitirle el acceso 2 veces (Puedes marcar la casilla para permitir siempre el acceso desde ese PC, pero no lo recomiendo)
### En Termux
1. Desde Android ingresa a Termux y ejecuta los siguientes comandos (aquí debes ingresar la IP estática que definiste en el Wi-Fi de tu Android.)

    ```bash
    adb connect <Tu dirección IP>:5555
    ```
    **Ejemplo:** `adb connect 127.0.0.1:5555`
    
    ```bash
    adb kill-server
    ```
    ```bash
    adb devices
    ```
2.	Ejecutar el script
    ```bash
    ./exclr_es.sh
    ```

## Iniciar
1. Abrir Termux en Android.
2. Ejecutar el el comando `./exclr_es.sh`.
3. Sigue las instrucciones en el menú interactivo.
4. Utiliza la opción 4 en el menú principal del script para forzar la detención de Termux.

### IMPORTANTE
La desventaja es que las `Opciones de desarrollador` debe mantenerse habilitado para que funcione el script. En caso de desactivar esta opción, seguir los siguientes pasos:
1. Conectar el Android al PC mediante cable.
2. En Windows, abrir `Minimal ADB and Fastboot Tool` y ejecutar el comando:
    ```bash
    adb tcpip 5555
    ```
3. En Termux, ejecutar el comando
    ```bash
    adb connect <Tu dirección IP>:5555
    ```
    ```bash
    adb devices
    ```
4. Esto debería solucionar y ya puedes [iniciar](#iniciar) de nuevo el script.


## Exclusión
Para excluir las apps que no deseas que se detengan o se quiten los permisos, puedes modificar el script `xclear_es.py` en la línea 47. Aquí agregas el nombre del paquete que pertenece a tu app de exclusión.

```bash
exclude_packages = ["com.whatsapp",             # Whatsapp
                    "com.facebook.orca",        # Messenger
                    "com.touchtype.swiftkey",   # Teclado
                    "com.microsoft.launcher",   # Launcher, pantalla principal
                    "com.android.systemui",     # Fondo de pantalla
                    "com.termux"]               # Termux, se cierra con la Opción "4. Salir".
```

## Contribuciones

¡Tu contribución es bienvenida! Si encuentras mejoras o tienes sugerencias, no dudes en contribuir. Abre un problema para discutir cambios o envía una solicitud de extracción con tus mejoras.

---

*Este archivo fue creado por Greg Jara, Ingeniero en Sistemas y Computación.*
