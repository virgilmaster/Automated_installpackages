class checker:
    def __init__(self,filename):
        self.filename = filename

    @property
    def versioncheck(self):
        try:
            from functions.filehandler import filesdetails
            import os,re,string,platform
        except ImportError as err:
            raise err

        os_result = platform.system()
        file_name = self.filename

        fileresult = filesdetails(file_name)
        namelist = fileresult.namefilter
        versionlist = fileresult.versionfilter
        '''
        Self testing function:
        list of the packages name
        '''
        files_read = filesdetails(file_name)
        final_num = files_read.counter
        requirefiles = files_read.readinfo
        
        numbers = int(final_num)
        if os_result == 'Windows':
            uninstall_list = []
            z = 0
            while z < numbers:
                packages_installed = os.popen('pip list | findstr' + ' ' + namelist[z]) 
                result_installed = packages_installed.readlines()     
                packages_installed.close()                              
                installed_version = str(result_installed).split(" ")[-1]
                final_installed = (re.sub('[%s]' % re.escape(string.punctuation), '', installed_version)).replace("n","")
                package_names = namelist[z]
                final_version = versionlist[z]
                pack_details = str(requirefiles[z]).split(',')[0].replace("['",'')
                '''   
                God plz bless me,let it run.
                '''
                if final_installed != final_version:
                    print('Prepare to download the' + ' ' + package_names)
                    uninstall_list.append(pack_details)
                    
                    print('{:>^89}'.format(">")) 
                elif final_installed == final_version:
                    print(package_names,'have no necessary to install')
                    print('{:>^89}'.format(">"))
                z += 1
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
                pack_details = str(requirefiles[z]).split(',')[0].replace("['",'')
                '''   
                Plz bless me,let it run.
                '''
                if final_installed != final_version:
                    print('Prepare to download the' + ' ' + package_names)
                    uninstall_list.append(pack_details)
                    print('{:>^89}'.format(">")) 
                elif final_installed == final_version:
                    print(package_names,'have no necessary to install')
                    print('{:>^89}'.format(">"))

            return uninstall_list 