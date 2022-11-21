class wizard():
    def __init__(self,sourcename):
        self.sourcename = sourcename

    @property
    def spellmagic(self):
        try:
            from collector import spiders
            from inspector import checker
            from threading import Lock
            from multiprocessing import Lock as Lk
            import os,platform,time
        except ImportError as error:
            raise error
        lock = Lock()
        source_name = self.sourcename
        file_name = 'requirements.txt'
        checker_pack = checker(file_name)
        uninstall_pack = checker_pack.versioncheck
        try:
            for j in range(len(uninstall_pack)):
                lock.acquire()
                final_uninstall = uninstall_pack[j]
                butterfly = spiders(source_name,final_uninstall)
                butterfly.downloader
                lock.release()
        except Exception as err:
            raise err
        else:
            print('Resources download fail',source_name,'have some problem')
            time.sleep(1)

        
