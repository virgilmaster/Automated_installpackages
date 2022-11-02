import os
import time
import datetime
from automation_upgrade import read_requirements
from automation_upgrade import handle_packages
import platform





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
    
    print("You will installed " + output_num + "Python packages")
    for i in range(numbers):
        package_detail = str(pack_information[i])
        package_result = package_detail.split("'")[1].split("'")[0]
        converted_result = package_result.split(",")[0]
        print(converted_result + "Plz make sure it's the correct version packages you want to installed on your computer!")


# Not a wonderful functions,will soon increase the fucntion.
# Next time will design in the class
def installation_packages():
    try:
        os.system('python get_download.py')
    except Exception as err:
        print(err)
    else:
        print("Failed to download the resource!!!")


if __name__ == '__main__':
    check_packages()
    installation_packages()

