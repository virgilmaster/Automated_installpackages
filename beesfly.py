import time
import threading
from threading import Lock
from collector import spiders


class wizard():
    def __init__(self,filename):
        self.filename = filename

    def spellmagic(self,x):
        try:
            from collector import spiders
            from inspector import checker
            import os,platform
        except ImportError as error:
            raise error
        lock = Lock()
        file_name = self.filename
        os_result = platform.system()
        checker_pack = checker(os_result,file_name)
        uninstall_pack = checker_pack.versioncheck
        try:
            for j in range(len(uninstall_pack)):
                final_uninstall = uninstall_pack[j]
                butterfly = spiders(x,final_uninstall)
                butterfly.downloader()
                lock.release()
        except Exception as err:
            raise err
        else:
            print('Resources download fail')
            time.sleep(1)

        
