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

    print("\n** WARNING! **")
    print(f"You are about to affect {total_packages} applications of '{usr}' with '{operation_name}'")

    if input("Do you want to continue? (1. Yes, 0. No): ") == "0":
        print("Operation canceled. No changes were made.")
        return

    with tqdm(total=total_packages, desc=f"Progress ({operation_name})", unit="app", position=1, leave=False) as progress_bar:
        for package_name in package_names:
            sys.stdout.write(f"\rProcessing package: {package_name.ljust(max_package_name_length)}")
            sys.stdout.flush()

            if "Force stop" in operation_name:
                execute_adb_command(["adb", "shell", "am", "force-stop", package_name])
            if "Remove permissions" in operation_name:
                execute_adb_command(["adb", "shell", "pm", "reset-permissions", package_name])
            if "Force stop and remove permissions" in operation_name:
                execute_adb_command(["adb", "shell", "am", "force-stop", package_name])
                execute_adb_command(["adb", "shell", "pm", "reset-permissions", package_name])

            progress_bar.update(1)

    print("\r" + " " * (len(max(package_names, key=len)) + 18) + "\r")
    print(f"Operation '{operation_name}' completed on {len(package_names)} applications.")

def main():
    while True:
        clear_screen()

        print("*******************************************")
        print("* ANDROID APPLICATION MANAGEMENT WITH ADB *")
        print("********************************************\n")
        print("This script provides an interface to manage applications on Android devices using ADB (Android Debug Bridge).")
        print("It allows forcing stop and resetting permissions for all applications, only for the user, or only for the system.\n")
        print("** WARNING! **")
        print("Misuse of these functions can cause problems with the normal operation of applications and the system.")
        print("Use this code responsibly. We are not responsible for any problems arising from misuse.\n")


        print("********************\n* CHOOSE AN OPTION *\n********************")
        print("1. User Applications")
        print("2. System Applications")
        print("3. All Applications (User and System)")
        print("4. Exit")

        choice = input("Enter the option number [1 ~ 4]: ")

        if choice == "4":
            break
        elif choice in ["1", "2", "3"]:
            usr = "User" if choice == "1" else ("System" if choice == "2" else "User and System")
            #operation_name = input("\nSelect the operation:\n (1. Force stop, 2. Remove permissions, 3. Force stop and remove permissions): ")
            print ("\n\n",usr,"APPLICATIONS :: What do you want to do?\n1. Force stop\n2. Remove permissions\n3. Force stop and remove permissions")
            operation_name = input("\nSelect the operation: ")

            if operation_name in ["1", "2", "3"]:
                package_names = run_adb_command(["adb", "shell", "pm", "list", "packages", "-3"]) if choice == "1" else (
                    run_adb_command(["adb", "shell", "pm", "list", "packages", "-s"]) if choice == "2" else
                    run_adb_command(["adb", "shell", "pm", "list", "packages"])
                )

                operation_name = (
                    "Force stop and remove permissions" if operation_name == "3" else
                    "Force stop" if operation_name == "1" else
                    "Remove permissions"
                )

                process_packages(package_names, operation_name, usr)
                input("\nPress Enter to continue...")
            else:
                print("Invalid operation. Select a valid operation (1, 2, 3).\n")
        else:
            print("Invalid option. Select a valid option (1, 2, 3, 4).\n")

if __name__ == "__main__":
    main()
