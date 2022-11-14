import os
import requests
from jmespath import search
import time
import platform
from sourceholder import mirrors
from filehandler import filesdetails



class spiders:
    def __init__(self,names):
        self.names = names
        

    def downloader(self):
        os_result = platform.system()
        file_name = filesdetails(str(os_result),'requirements.txt')
        final_num = file_name.counter
        pack_info = file_name.readinfo
        numb = int(final_num)
        final_names = self.names
        for i in range(numb):
            package_detail = str(pack_info[i])
            package_result = package_detail.split("'")[1].split("'")[0]
            download_pool = mirrors(str(final_names))
            final_pools = download_pool.mirrorspools
            domain = str(final_pools).split(' ')[1].replace("'", "").replace(",", "")
            link = str(final_pools).split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
            resp = requests.get('http://' + domain)
            code_result = resp.status_code
            if code_result != 200:
                print(final_names + ' ' + 'requests error')
                raise Exception(final_names + ' ' + 'can not download the resources')
            else:
                print('Perpare to download the resources!!!')
                time.sleep(5)
                begin_time = time.time()
                os.system("pip install " + package_result.replace(",","") + " -i " + link + " --trusted-host " + domain)
                print('{:>^89}'.format(">"))
                end_time  = time.time()
                print("The total time is: %s" % (end_time - begin_time))



