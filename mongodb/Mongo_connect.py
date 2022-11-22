
class mongoconnect:
    def __init__(self,port,ip):
        self.port = port 
        self.ip = ip
        

    def datafresh(self):
        try:
            import pymongo
            import datetime,platform,os
        except ImportError as error:
            raise error 
        port_result = self.port
        ip_result = self.ip
        pg = pymongo.MongoClient
        mongo_client = pg(ip_result,port_result)  
        data_base = mongo_client['Daily_working']
        collection_table = data_base['Download_record']
        c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
        file = "download_" + c_t + ".log"
        os.getcwd()
        os.chdir('downloadlog')
        operation_system = platform.system()
        if operation_system == 'Windows':
            log_num = os.popen('type' + ' ' + file + "| " + 'find /v /c""')
            output_num = log_num.readlines()
            final_num = str(output_num[0]).replace("\n",'')
            log_num.close()
        elif operation_system == 'Linux':
            log_num = os.popen('cat' + file + '| wc -l')
            output_num = log_num.readlines()
            final_num = str(output_num[0]).replace("\n",'')
            log_num.close()
        with open(file,"r",encoding="utf-8") as f:
            reader = f.readlines()
            x = 0
            while x < int(final_num):
                action_result = str(reader[x]).split(" ")[1:4]
                user_result = str(reader[x]).split(" ")[0]
                time_result = str(reader[x]).split(" ")[12:14]
                package_result = str(reader[x]).split(" ")[5]  
                log = {
                    'username' : user_result,
                    'actions' : action_result,
                    'time' : time_result,
                    'package' : package_result
                }
                print('Save messages the' + ' ' + str(x))
                x += 1
        

if __name__ == '__main__':
    db_port = int('27017')
    ip_addr = '127.0.0.1'
    MGO = mongoconnect(db_port,ip_addr)
    MGO.datafresh()
    