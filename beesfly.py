import time
import threading
from threading import Lock
from collector import spiders


class wizard():
    def __init__(self,sourcename):
        self.sourcename = sourcename

    def spellmagic(self):
        try:
            from collector import spiders
            from inspector import checker
            import os,platform
        except ImportError as error:
            raise error
        lock = Lock()
        source_name = self.sourcename
        file_name = 'requirements.txt'
        os_result = platform.system()
        checker_pack = checker(os_result,file_name)
        uninstall_pack = checker_pack.versioncheck
        try:
            for j in range(len(uninstall_pack)):
                final_uninstall = uninstall_pack[j]
                butterfly = spiders(source_name,final_uninstall)
                butterfly.downloader()
                lock.release()
        except Exception as err:
            raise err
        else:
            print('Resources download fail',source_name,'have some problem')
            time.sleep(1)

        
