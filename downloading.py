import os
import time
import datetime
from automation_upgrade import read_requirements
from automation_upgrade import handle_packages
import platform
import threading


# Json data from dictionary
# def installation_mirrors(mirror_pools):
#     with open("Mirrors_links.json", "w") as mirrors_file:
#         mirrors_file.write(str(mirror_pools))
#         mirrors_file.close()
#     print("Wait a moment,loading the settings")

def check_packages():
    operation_system = platform.system()
    if operation_system == "Windows":
        pack_num = os.popen('type requirements.txt | find /v /c""')
        username = os.getlogin()
        output_num = pack_num.read()
        pack_num.close()
    elif operation_system == "Linux":
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        username = command_username.read()
        output_num = pack_num.read()
        command_username.close()
        pack_num.close()

    pack_information = read_requirements("requirements.txt")
    numbers = int(output_num)
    print(numbers)
    for i in range(numbers):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        converted_result = package_result.split(",")[0]
        package_names = package_result.split("==")[0]
        package_version = package_result.split("==")[1]
        print(package_names)



def installation_packages():
         os.system("")




if __name__ == '__main__':
    check_packages()
    installation_packages()

