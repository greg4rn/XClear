# Android Application Management with ADB

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setting Environment Variables](#setting-environment-variables)
4. [Connecting the Android Phone](#connecting-the-android-phone)
5. [Developer Mode and USB Debugging](#developer-mode-and-usb-debugging)
6. [Checking ADB Connection](#checking-adb-connection)
7. [Usage](#usage)
8. [Contributions](#contributions)

## Versión en Español

Visita el siguiente enlace: [Recursos](https://github.com/greg4rn/resources/blob/main/README_ES.md)

## Introduction

This script provides an interface for managing applications on Android devices using ADB (Android Debug Bridge). It allows forcing the stop and resetting permissions for all applications, only for the user, or only for the system.

**WARNING!**
Misuse of these functions can cause issues with the normal operation of applications and the system. Use this code responsibly. We are not responsible for any problems arising from misuse.

## Prerequisites

Before running the script, ensure you have the following components installed:

1. **ADB (Android Debug Bridge):**
   - If ADB is not installed, visit the [official Minimal ADB page](https://androidmtk.com/download-minimal-adb-fastboot-tool) and follow the installation instructions.

2. **Python 3.x:**
   - If Python 3.x is not installed, download it from the [official Python page](https://www.python.org/downloads/) and follow the installation instructions.

## Setting Environment Variables

After installing ADB and Python, add the following paths to your system's environment variables. This will make it easier to access these programs from any location in your terminal.

- For Python:
  - `%USERPROFILE%\AppData\Local\Programs\Python\Python311\`

- For ADB:
  - `C:\Program Files (x86)\Minimal ADB and Fastboot`

Adding these environment variables allows you to execute ADB and Python commands from any directory in your terminal.

## Connecting the Android Phone

Before running the script, make sure your Android phone is connected to the PC via a USB cable.

## Developer Mode and USB Debugging

For ADB to work correctly, enable Developer Mode and USB Debugging on your Android phone. Follow these general steps:

1. Go to your phone's settings.
2. Find the "About Phone" option and tap it several times until "Developer Options" appears.
3. Within "Developer Options," enable "USB Debugging."

**Note:** Disable "USB Debugging" after using the script for security reasons.

## Checking ADB Connection

To check if your Android phone is correctly connected to the PC via ADB, follow these steps:

1. Open your terminal (cmd, PowerShell, or your preferred terminal compatible with the added environment variables).
2. Run the following command: `adb devices`
3. You should see your Android device in the list of connected devices.

## Usage

1. Clone the repository or download the script.
2. Open your terminal.
3. Navigate to the directory where the script is located.
4. Run the script with the command `python script_name.py`.
5. Follow the instructions in the interactive menu.

## Contributions

Your contribution is welcome! If you find improvements or have suggestions, feel free to contribute. Open an issue to discuss changes or submit a pull request with your enhancements.

---

*This file was created by Greg Jara, Systems and Computer Engineer.*
