import os
import platform


class filesdetails:
    def __init__(self,op,filename):
        self.op = op
        self.filename = filename

    @property
    def counter(self):
        filename = self.filename
        if self.op == platform.system():
            pack_num = os.popen('type' + ' ' + filename + '| find /v /c""')
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\n", '')
            pack_num.close()         
        elif self.op == platform.system():
            pack_num = os.popen('cat requirements.txt | wc -l"')         
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\\n", '').replace('\n', '')
            pack_num.close()
            
        return final_num

    @property
    def readlines(self):
        filename = self.filename
        pack_information = []  
        file = open(filename,'r') 
        file_pack_information = file.readlines()
        for row in file_pack_information:  
            tmp_list = row.split(' ')
            tmp_list[-1] = tmp_list[-1].replace('\n',',')
            pack_information.append(tmp_list)
        return pack_information

