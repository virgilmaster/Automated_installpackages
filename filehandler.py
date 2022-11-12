import os
import platform


class files:
    def __init__(self,op,filename):
        self.op = op
        self.filename = filename
        # self.filepath = filepath
        # self.filetype = filetype

    @property
    def windowsfile(self):
        self.op == "Windows"
        pack_num = os.popen('type requirements.txt | find /v /c""')
        username = os.getlogin()
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\n", '')
        pack_num.close()
        print(final_num)

    def linuxfile(self):
        self.op == "Linux"
        pack_num = os.popen('cat requirements.txt | wc -l"')
        command_username = os.popen('whoami')
        username = command_username.read()
        output_num = pack_num.readlines()
        final_num = str(output_num[0]).replace("\\n", '').replace('\n', '')
        command_username.close()
        pack_num.close()
        print(final_num)

if __name__ == '__main__':
    object = files("Windows","requirements.txt")
    print(object.windowsfile)
