class spiders:
    def __init__(self,sourcenames,packagename):
        self.sourcenames = sourcenames
        self.packagename = packagename


    @property
    def downloader(self):
        try:
            import os,requests,time,platform
            from jmespath import search
            from source.sourceholder import mirrors
            from functions.filehandler import filesdetails
            
        except ImportError as e:
            raise e

        filesname = 'requirements.txt'
        require_txt = filesdetails(filesname)
        final_num = require_txt.counter
        pack_info = require_txt.readinfo
        numb = int(final_num)
        source_names = self.sourcenames
        uninstall_package = self.packagename

        for i in range(numb):
            package_detail = str(pack_info[i])
            package_result = package_detail.split("'")[1].split("'")[0]
            download_pool = mirrors(str(source_names))
            final_pools = download_pool.mirrorspools
            domain = str(final_pools).split(' ')[1].replace("'", "").replace(",", "")
            link = str(final_pools).split(' ')[3].replace("'", "").replace("}", "").replace("]", "")
            resp = requests.get('http://' + domain)
            code_result = resp.status_code

            if code_result != 200:
                print(source_names + ' ' + "'s requests error")
                raise Exception(source_names + ' ' + 'can not download the resources')

            else:
                print('Downloading the resources!')
                time.sleep(5)
                os.system("pip install " + uninstall_package + " -i " + link + " --trusted-host " + domain)
                print('{:>^89}'.format(">"))


