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
                Plz bless me,let it run.
                '''
                if final_installed == '[]':
                    uninstall_list.append(package_names) 
                elif final_installed == final_version:
                    print(package_names,'have no necessary to install')
                else:
                    uninstall_list.append(package_names) 
            return uninstall_list 


        elif os_result == 'Linux':
            for x in range(numbers):
                packages_installed = os.popen('pip list | grep' + ' ' + namelist[x])
                result_installed = packages_installed.readlines()     
                packages_installed.close()                              
                installed_version = str(result_installed).split(" ")[-1]
                final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
                package_names = namelist[x]
                final_version = versionlist[x]
                #print(package_names)
                '''   
                Plz bless me,let it run.
                '''
                if final_installed == '[]':
                    uninstall_list.append(package_names) 
                elif final_installed == final_version:
                    print(package_names,'have no necessary to install')
                else:
                    uninstall_list.append(package_names) 
            return uninstall_list 
