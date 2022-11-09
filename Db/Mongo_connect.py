import pymongo
 import datetime
import os 
import platform


# username  actions  time  object  details
def connection(db_port):
    pg = pymongo.MongoClient
    mongo_client = pg('XXX.XXX.XXX.XXX',db_port)  # Use your own ip address for mongo
    data_base = mongo_client['Daily_working']
    collection_table = data_base['Download_record']


def datafresh(filename):
    os.getcwd()
    os.chdir('downloadlog')
    with open(filename,"r",encoding="utf-8") as f:
        reader = f.readlines()
        print(type(reader))
        print(reader[1])

    operation_system = platform.system()
    if operation_system == 'Windows':
        log_num = os.popen('type' + ' ' + filename + "| " + 'find /v /c""')
        output_num = log_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        log_num.close()
        print(final_num)
    elif operation_system == 'Linux':
        log_num = os.popen('cat' + filename + '| wc -l')
        output_num = log_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        log_num.close()



if __name__ == '__main__':
    c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
    filename = "download_" + c_t + ".log"
    db_port = int('XXXX') # Use your own port 
    connection(db_port)
    datafresh(filename)
