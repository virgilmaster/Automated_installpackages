from filehandler import filesdetails
import os
import requests
from jmespath import search
import time
import platform
from sourceholder import mirrors
from filehandler import filesdetails



class spiders:
    def __init__(self,sdname,sdmode):
        self.sdname = sdname
        self.sdmode = sdmode

    def downloader(self):
        file_name = filesdetails('Windows','requirements.txt')
        final_num = file_name.counter
        pack_info = file_name.readlines
        numb = int(final_num)
        for i in range(numb):
            package_detail = str(pack_info[i])
            package_result = package_detail.split("'")[1].split("'")[0]
            download_pool = mirrors(self.sdname)
            domain = str(download_pool).split(' ')[1].replace("'", "").replace(",", "")
            link = str(download_pool).split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
            resp = requests.get('http://' + domain)
            code_result = resp.status_code
            if code_result != 200:
                print(self.sdname + ' ' + 'requests error')
                raise Exception(self.sdname + ' ' + 'can not download the resources')
            else:
                print('Perpare to download the resources!!!')
                time.sleep(5)
                begin_time = time.time()
                os.system("pip install " + package_result.replace(",","") + " -i " + aliyun_link + " --trusted-host " + aliyun_domain)
                print('{:>^89}'.format(">"))
                end_time  = time.time()
                print("The total time is: %s" % (end_time - begin_time))


a = spiders('aliyun','thread')
a.downloader()
