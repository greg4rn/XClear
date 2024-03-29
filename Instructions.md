# FIRST PART
## ANDROID - TERMUX
First, we need to update all installed packages in Termux to the latest available versions.

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
Next, we will download the 2 necessary files xclear.py (script) and exclr.sh (executable).
```bash
wget https://raw.githubusercontent.com/greg4rn/resources/main/xclear.py ; wget https://raw.githubusercontent.com/greg4rn/resources/main/exclr.sh
```

### Details:
- When we run `pkg upgrade`, we will be prompted with some questions, but only on the 1st question do we confirm the installation with a `Y` and then press `Enter`. There will be about 6 more questions, and for these, we just press `Enter` to leave it with the default option, which is `N`.
- `android-tools`: It is used to interact with connected Android devices and execute ADB commands.
- `python3`: It is used to execute the Python script.
- `tqdm`: It displays a visual progress bar of operations.
- `wget`: It allows downloading files from the web. However, you can use the command `nano xclear.py` to create our Python file, there you should paste the code I'm sharing with you and don't forget to save the file before exiting the editor.

# SECOND PART
# Android Terminal Configuration
1. Set a static IP on your Android terminal when connecting to your trusted Wi-Fi network.
2. Enable the `Developer Options` or `Developer Settings` mode. The option to activate this varies for each Android terminal. You can search on YouTube for "How to activate Developer Options".
3. Connect your Android terminal to the PC via cable.

# Configuration from Windows:
1. Download and install the latest version of Minimal ADB and Fastboot Tool (all versions).
2. Open "Minimal ADB and Fastboot".
3. Run the following commands:
    ```bash
    adb kill-server
    ```
    ```bash
    adb tcpip 5555
    ```
    Now, a window should appear on your Android terminal that you should allow access to twice (You can check the box to always allow access from this PC, but I don't recommend it).

Configuration from TERMUX on your Android Terminal:
1. From your Android terminal, open Termux and execute the following commands (here you should enter the static IP you defined on your Android terminal; this is the static IP I configured on my Android terminal: 192.168.1.50, you should replace it with `your.static.ip.address:5555`).
    ```bash
    adb connect 192.168.1.50:5555
    ```
    ```bash
    adb kill-server
    ```
    ```bash
    adb devices
    ```
2. We still need to give execution permission to our script, so we execute the command:
    ```bash
    chmod +x exclr_es.sh
    ```
3.	Finally, we can execute the command:
    ```bash
    ./exclr_es.sh
    ```
## To rerun the script
1. Open Termux and execute the following:
    ```bash
    ./exclr_es.sh
    ```
2. Similarly, don't forget to close the execution by selecting option 4.
  IMPORTANT: The disadvantage is that Developer Options must remain enabled for the script to work. If you disable this option, an external device (such as a PC with android-tools) is needed to execute ADB commands to the Android terminal.


## DID SOMETHING GO WRONG?
Let's start over, reset everything with this setup.
1. In Developer Options, select the "Revoke devices" option (it's below USB Debugging).
2. Turn off USB Debugging.
3. Turn off Developer Options.
4. In the Termux app, execute:
    ```bash
    adb kill-server
    ```
    ```bash
    exit
    ```
5. Android: Force stop Termux and clear the cache of this app.
6. In Windows, open "Minimal ADB and Fastboot" and execute: adb kill-server.
7. Let's start from the SECOND PART! (But if you clear the data from Termux, you must start from the FIRST PART again)
