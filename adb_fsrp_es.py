import subprocess
from tqdm import tqdm
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_adb_command(command):
    output = subprocess.check_output(command, text=True)
    return [line.strip().replace("package:", "") for line in output.split('\n') if line.strip()]

def execute_adb_command(command):
    return subprocess.call(command)

def process_packages(package_names, operation_name, usr):
    total_packages = len(package_names)
    max_package_name_length = max(len(package_name) for package_name in package_names)

    print("\n** ¡ADVERTENCIA! **")
    print(f"Estás a punto de afectar a {total_packages} aplicaciones del '{usr}' con '{operation_name}'")

    if input("¿Deseas continuar? (1. Si, 0. No): ") == "0":
        print("Operación cancelada. No se realizaron cambios.")
        return

    with tqdm(total=total_packages, desc=f"Progreso ({operation_name})", unit="app", position=1, leave=False) as progress_bar:
        for package_name in package_names:
            sys.stdout.write(f"\rProcesando paquete: {package_name.ljust(max_package_name_length)}")
            sys.stdout.flush()

            if "Forzar detención" in operation_name:
                execute_adb_command(["adb", "shell", "am", "force-stop", package_name])
            if "Remover permisos" in operation_name:
                execute_adb_command(["adb", "shell", "pm", "reset-permissions", package_name])
            if "Forzar detención y remover permisos" in operation_name:
                execute_adb_command(["adb", "shell", "am", "force-stop", package_name])
                execute_adb_command(["adb", "shell", "pm", "reset-permissions", package_name])

            progress_bar.update(1)

    print("\r" + " " * (len(max(package_names, key=len)) + 18) + "\r")
    print(f"Se completó la operación '{operation_name}' en {len(package_names)} aplicaciones.")

def main():
    while True:
        clear_screen()

        print("************************************************************")
        print("* CÓDIGO DE ADMINISTRACIÓN DE APLICACIONES ANDROID CON ADB *")
        print("************************************************************\n")
        print("Este script brinda una interfaz para gestionar aplicaciones en dispositivos Android utilizando ADB (Android Debug Bridge).")
        print("Permite forzar la detención y restablecer permisos en todas las aplicaciones, solo del usuario o solo del sistema.\n")
        print("** ¡ADVERTENCIA! **")
        print("El mal uso de estas funciones puede causar problemas en el funcionamiento normal de las aplicaciones y del sistema.")
        print("Utiliza este código con responsabilidad. No nos hacemos responsables por cualquier inconveniente derivado de su uso indebido.\n")


        print("********************\n* ELIGE UNA OPCIÓN *\n********************")
        print("1. Aplicaciones del USUARIO")
        print("2. Aplicaciones del SISTEMA")
        print("3. TODAS las aplicaciones (USUARIO y SISTEMA)")
        print("4. Salir")

        choice = input("Ingresa el número de la opción [1 ~ 4]: ")

        if choice == "4":
            break
        elif choice in ["1", "2", "3"]:
            usr = "USUARIO" if choice == "1" else ("SISTEMA" if choice == "2" else "USUARIO y SISTEMA")
            #operation_name = input("\nSelecciona la operación:\n (1. Forzar detención, 2. Remover permisos, 3. Forzar detención y remover permisos): ")
            print ("\n\nAPLICACIONES DEL",usr,":: ¿Qué deseas hacer?\n1. Forzar detención\n2. Remover permisos\n3. Forzar detención y remover permisos")
            operation_name = input("\nSelecciona la operación: ")

            if operation_name in ["1", "2", "3"]:
                package_names = run_adb_command(["adb", "shell", "pm", "list", "packages", "-3"]) if choice == "1" else (
                    run_adb_command(["adb", "shell", "pm", "list", "packages", "-s"]) if choice == "2" else
                    run_adb_command(["adb", "shell", "pm", "list", "packages"])
                )

                operation_name = (
                    "Forzar detención y remover permisos" if operation_name == "3" else
                    "Forzar detención" if operation_name == "1" else
                    "Remover permisos"
                )

                process_packages(package_names, operation_name, usr)
                input("\nPresiona Enter para continuar...")
            else:
                print("Operación no válida. Selecciona una operación válida (1, 2, 3).\n")
        else:
            print("Opción no válida. Selecciona una opción válida (1, 2, 3, 4).\n")

if __name__ == "__main__":
    main()
