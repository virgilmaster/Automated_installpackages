class filesdetails:
    def __init__(self,op,filename):
        self.op = op
        self.filename = filename

    @property
    def counter(self):
        import os
        filename = self.filename
        if self.op == 'Windows':
            pack_num = os.popen('type' + ' ' + filename + '| find /v /c""')
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\n", '')
            pack_num.close()      
        elif self.op == 'Linux':
            pack_num = os.popen('cat requirements.txt | wc -l')         
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\\n", '').replace('\n', '')
            pack_num.close()
        return final_num

    @property
    def readinfo(self):
        filename = self.filename
        pack_information = []  
        file = open(filename,'r') 
        file_pack_information = file.readlines()
        for row in file_pack_information:  
            tmp_list = row.split(' ')
            tmp_list[-1] = tmp_list[-1].replace('\n',',')
            pack_information.append(tmp_list)
        return pack_information

    @property
    def uninstallpack(self):
        try:
            import platform
            from filehandler import filesdetails

        except ImportError as e:
            print(e)

        os_result = platform.system()
        result_pack = filesdetails(str(os_result),'requirements.txt')
        final_num = result_pack.counter
        pack_info = result_pack.readinfo
        numbers = int(final_num)
        
        try:
            import re,string
        except ImportWarning as e:
            print('Dear guests your python lib have not re and string module,plz download from internet')
        for i in range(numbers):  
            package_detail = str(pack_info[i]) 
            package_result = package_detail.split("'")[1].split("'")[0]
            package_names = package_result.split("==")[0]  
            package_version = package_result.split("==")[1]
            final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)
        # Self testing functions
        # ======================================================
        try:
            import os
        except ImportError as e:
            print(e)
        if os_result == "Windows":
            packages_installed = os.popen("pip list | findstr " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()                              
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
            

            
            #HashMap = {}
            uninstall_list = []
            if installed_version == '[]':
                print(package_names +  " have not be installed")
                print("Start launch the webspiders,to download the new " + package_names)
                uninstall_list.append(package_names)

  
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")

            else:
                print("The packages's version is " + installed_version)
                print("Start to change " + package_names + "'s version,plz wait a moment~.~")
                uninstall_list.append(package_names)
               
            print(uninstall_list)    
            

        elif os_result == "Linux":
            packages_installed = os.popen("pip list | grep " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
    

        
            if installed_version == '[]':
                print(package_names +  " have not be installed")
                print("Start launch the webspiders,to download the new " + package_names)
                
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")
            else:
                print("The packages's version is " + installed_version)
                print("Start to change" + package_names + "'s version,plz wait a moment~.~")
              
            return uninstall_list




