class checker:
    def __init__(self,opsys,filename):
        self.opsys = opsys
        self.filename = filename

    @property
    def versioncheck(self):
        try:
            from filehandler import filesdetails
            import os,re,string
        except ImportError as err:
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
        files_read = filesdetails(str(os_result),'requirements.txt')
        final_num = files_read.counter
        numbers = int(final_num)
        if os_result == 'Windows':
            uninstall_list = []
            for x in range(numbers):
                packages_installed = os.popen('pip list | findstr' + ' ' + namelist[x]) 
                result_installed = packages_installed.readlines()     
                packages_installed.close()                              
                installed_version = str(result_installed).split(" ")[-1]
                final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
                package_names = namelist[x]
                final_version = versionlist[x]
                '''   
                Plz God bless me,let it run.
                '''
                if final_installed == '[]':
                    print('The' + package_names + 'is not installed on the computer')
                    uninstall_list.append(package_names) 
                elif final_installed == final_version:
                    print(package_names,'have no necessary to install')
                else:
                    print('The' + package_names + 'is not correct version on the computer')
                    os.system('pip uninstall' + package_names)
                    uninstall_list.append(package_names)

            return uninstall_list 


        elif os_result == 'Linux':
            uninstall_list = []
            for x in range(numbers):
                packages_installed = os.popen('pip list | grep' + ' ' + namelist[x])
                result_installed = packages_installed.readlines()     
                packages_installed.close()                              
                installed_version = str(result_installed).split(" ")[-1]
                final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
                package_names = namelist[x]
                final_version = versionlist[x]
                '''   
                Plz bless me,let it run.
                '''
                if final_installed == '[]':
                    print('The' + package_names + 'is not installed on the computer')
                    uninstall_list.append(package_names) 
                elif final_installed == final_version:
                    print(package_names,'have no necessary to install')
                else:
                    print('The' + package_names + 'is not correct version on the computer')
                    os.system('pip uninstall' + package_names)
                    uninstall_list.append(package_names)

            return uninstall_list 
