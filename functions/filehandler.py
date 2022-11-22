class filesdetails:
    def __init__(self,filename):
        self.filename = filename

    @property
    def counter(self):
        import os,platform
        file_name = self.filename
        os_result = platform.system()
        if os_result == 'Windows':
            pack_num = os.popen('type' + ' ' + file_name + ' | find /v /c""')
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\n", '')
            pack_num.close()
        elif os_result == 'Linux':
            pack_num = os.popen('cat' + ' ' + file_name + ' | wc -l')
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\\n", '').replace('\n', '')
            pack_num.close()
        return final_num


    @property
    def readinfo(self):
        file_name = self.filename
        pack_information = []
        file = open(file_name)
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
            from functions.filehandler import filesdetails
            import re,string

        except ImportError as e:
            raise e

        file_name = self.filename
        os_result = platform.system()
        result_pack = filesdetails(file_name)
        final_num = result_pack.counter
        pack_info = result_pack.readinfo
        numbers = int(final_num)
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
            from functions.filehandler import filesdetails
            import re,string
        except ImportError as e:
            raise e
        file_name = self.filename
        os_result = platform.system()
        result_pack = filesdetails(file_name)
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
