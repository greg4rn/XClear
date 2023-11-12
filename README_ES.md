# Administración de Aplicaciones Android con ADB

## Índice

1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno)
4. [Conexión del Teléfono Android](#conexión-del-teléfono-android)
5. [Modo Programador y Depuración USB](#modo-programador-y-depuración-usb)
6. [Comprobación de la Conexión con ADB](#comprobación-de-la-conexión-con-adb)
7. [Uso](#uso)
8. [Contribuciones](#contribuciones)

## English version 

Visit the next link: [Resources](https://github.com/greg4rn/resources)

## Introducción

Este script proporciona una interfaz para gestionar aplicaciones en dispositivos Android utilizando ADB (Android Debug Bridge). Permite forzar la detención y restablecer permisos en todas las aplicaciones, solo del usuario o solo del sistema.

**¡ADVERTENCIA!**
El mal uso de estas funciones puede causar problemas en el funcionamiento normal de las aplicaciones y del sistema. Utiliza este código con responsabilidad. No nos hacemos responsables por cualquier inconveniente derivado de su uso indebido.

## Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalados los siguientes componentes:

1. **ADB (Android Debug Bridge):**
   - Si no tienes instalado ADB, visita la [página oficial de Minimal ADB](https://androidmtk.com/download-minimal-adb-fastboot-tool) y sigue las instrucciones de instalación.

2. **Python 3.x:**
   - Si no tienes instalado Python 3.x, descárgalo desde la [página oficial de Python](https://www.python.org/downloads/) y sigue las instrucciones de instalación.

## Configuración de Variables de Entorno

Después de instalar ADB y Python, agrega las siguientes rutas a las variables de entorno de tu sistema. Esto facilitará el acceso a estos programas desde cualquier ubicación en tu terminal.

- Para Python:
  - `%USERPROFILE%\AppData\Local\Programs\Python\Python311\`

- Para ADB:
  - `C:\Program Files (x86)\Minimal ADB and Fastboot`

Añadir estas variables de entorno permitirá ejecutar comandos ADB y Python desde cualquier directorio en tu terminal.

## Conexión del Teléfono Android

Antes de ejecutar el script, asegúrate de tener tu teléfono Android conectado al PC mediante un cable USB.

## Modo Programador y Depuración USB

Para que ADB funcione correctamente, activa el Modo Programador y la Depuración USB en tu teléfono Android. Sigue estos pasos generales:

1. Ve a la configuración del teléfono.
2. Busca la opción "Acerca del teléfono" y tócala varias veces hasta que aparezca "Modo Desarrollador".
3. Dentro de "Opciones de Desarrollador", activa "Depuración USB".

**Nota:** Desactiva la "Depuración USB" después de usar el script por razones de seguridad.

## Comprobación de la Conexión con ADB

Para comprobar si tu teléfono Android está correctamente conectado a la PC a través de ADB, sigue estos pasos:

1. Abre tu terminal (cmd, PowerShell o tu terminal preferido compatible con las variables de entorno).
2. Ejecuta el siguiente comando: `adb devices`
3. Deberías ver tu dispositivo Android en la lista de dispositivos conectados.

## Uso

1. Clona el repositorio o descarga el script.
2. Abre tu terminal.
3. Navega al directorio donde se encuentra el script.
4. Ejecuta el script con el comando `python nombre_del_script.py`.
5. Sigue las instrucciones en el menú interactivo.

## Contribuciones

¡Tu contribución es bienvenida! Si encuentras mejoras o tienes sugerencias, no dudes en contribuir. Abre un problema para discutir cambios o envía una solicitud de extracción con tus mejoras.

---

*Este archivo fue creado por Greg Jara, Ingeniero en Sistemas y Computación.*
