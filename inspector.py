class checker:

    def __init__(self,opsys,filename):
        self.opsys = opsys
        self.filename = filename

    @property
    def versioncheck(self):
        try:
            from filehandler import filesdetails
        except ImportError as e:
            raise e

        os_result = self.opsys
        file_name = self.filename
        tgfiles = filesdetails(os_result,file_name)
        # print(tgfiles.filefilter)

        try:
            import os,re,string
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
                uninstall_list.append(package_names) # 需要安装新的包


            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")

            else:
                uninstall_list.append(package_names) # 需要安装新的包
            return uninstall_list
                
            

        elif os_result == "Linux":
            packages_installed = os.popen("pip list | grep " + package_names) 
            result_installed = packages_installed.readlines()     
            packages_installed.close()
            installed_version = str(result_installed).split(" ")[-1]
            final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
    

            uninstall_list = []
            if installed_version == '[]':
                uninstall_list.append(package_names) # 需要安装新的包
                
            elif final_installed == final_version:
                print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")
            else:
                uninstall_list.append(package_names) # 需要安装新的包
            
            return uninstall_list
