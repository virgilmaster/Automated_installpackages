class checker:
    def __init__(self,opsys,filename):
        self.opsys = opsys
        self.filename = filename

    #@staticmethod
    @property
    def versioncheck(self):
        try:
            from filehandler import filesdetails
            import os,re,string
        except ImportError as err:
            print(err)
            raise err

        os_result = self.opsys
        file_name = self.filename

        fileresult = filesdetails(file_name,os_result)
        namelist = fileresult.namefilter
        versionlist = fileresult.versionfilter
        '''
        Test function:
        list of the packages name
        '''
        # print(namelist[0])
        # print(namelist[1])
        # print(versionlist[0])
        # print(versionlist[1])
        """
        Test pass
        Math teacher
        Powershell can call Python!!! 
        """
        files_read = filesdetails(str(os_result),'requirements.txt')
        final_num = files_read.counter
        numbers = int(final_num)
        if os_result == 'Windows':
            for x in range(numbers):
                packages_installed = os.popen('pip list | findstr' + ' ' + namelist[x]) 
                result_installed = packages_installed.readlines()     
                packages_installed.close()                              
                installed_version = str(result_installed).split(" ")[-1]
                final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
                print(result_installed) # 结果测试
                print(type(result_installed))
                

        elif os_result == 'Linux':
            for x in range(numbers):
                packages_installed = os.popen('pip list | grep' + ' ' + namelist[x])
                result_installed = packages_installed.readlines()     
                packages_installed.close()                              
                installed_version = str(result_installed).split(" ")[-1]
                final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
                print(result_installed)

        # if os_result == "Windows":


        # elif os_result == "Linux":       

        # if os_result == "Windows":
        #     packages_installed = os.popen("pip list | findstr " + package_names) 
        #     result_installed = packages_installed.readlines()     
        #     packages_installed.close()                              
        #     installed_version = str(result_installed).split(" ")[-1]
        #     final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
            

            
        #     #HashMap = {}
        #     uninstall_list = []
        #     if installed_version == '[]':
        #         uninstall_list.append(package_names) # 需要安装新的包


        #     elif final_installed == final_version:
        #         print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")

        #     else:
        #         uninstall_list.append(package_names) # 需要安装新的包
        #     return uninstall_list
                
            

        # elif os_result == "Linux":
        #     packages_installed = os.popen("pip list | grep " + package_names) 
        #     result_installed = packages_installed.readlines()     
        #     packages_installed.close()
        #     installed_version = str(result_installed).split(" ")[-1]
        #     final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
    

        #     uninstall_list = []
        #     if installed_version == '[]':
        #         uninstall_list.append(package_names) # 需要安装新的包
                
        #     elif final_installed == final_version:
        #         print("The " + package_names + " is in the same version,no necessary to install " + package_names + " again")
        #     else:
        #         uninstall_list.append(package_names) # 需要安装新的包
            
        #     return uninstall_list

