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
    def versionfilter(self):
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
            raise e

        version_list = []
        j = 0
        while j < numbers:
            package_detail = str(pack_info[j]) 
            package_result = package_detail.split("'")[1].split("'")[0]
            package_names = package_result.split("==")[0]  
            package_version = package_result.split("==")[1]
            final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)
            version_list.append(final_version)
            j += 1
        return version_list


    @property
    def namefilter(self):
        try:
            import platform
            from filehandler import filesdetails
            import re,string
        except ImportError as e:
            raise e 

        os_result = platform.system()
        result_pack = filesdetails(str(os_result),'requirements.txt')
        final_num = result_pack.counter
        pack_info = result_pack.readinfo
        numbers = int(final_num)
        j = 0
        name_list = []
        while j < numbers: 
            package_detail = str(pack_info[j]) 
            package_result = package_detail.split("'")[1].split("'")[0]
            package_names = package_result.split("==")[0]  
            package_version = package_result.split("==")[1]
            final_version = re.sub('[%s]' % re.escape(string.punctuation), '', package_version)
            name_list.append(package_names)
            j += 1
        return name_list

