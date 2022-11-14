import os
import platform


class files:
    def __init__(self,op,filename):
        self.op = op
        self.filename = filename
        # self.filepath = filepath
        # self.filetype = filetype

    @property
    def counter(self):

        filename = self.filename
        if self.op == platform.system():
            pack_num = os.popen('type' + ' ' + filename + '| find /v /c""')
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\n", '')
            pack_num.close()
            print('Oh dear guests your system is: ' + str(platform.system()))
            print(int(final_num))
            print(type(final_num))

        elif self.op == platform.system():
            pack_num = os.popen('cat requirements.txt | wc -l"')
            command_username = os.popen('whoami')           
            output_num = pack_num.readlines()
            final_num = str(output_num[0]).replace("\\n", '').replace('\n', '')
            command_username.close()
            pack_num.close()
            print(final_num)

        

if __name__ == '__main__':
    file1 = files("Windows","requirements.txt")
    print(file1.counter)
