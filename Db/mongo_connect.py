import pymongo
import datetime
import os 
import platform



def datafresh(filename,db_port,db_name,db_collection):
    os.getcwd()
    os.chdir('downloadlog')
    pg = pymongo.MongoClient
    mongo_client = pg('XXX.000.000.XXX',db_port)  # Your cidr address
    data_base = mongo_client[db_name]  # Your database name
    collection_table = data_base[db_collection] # Your collection name
    #collection_table.create_index("recorder_log") # Create index
    operation_system = platform.system()
    if operation_system == 'Windows':
        log_num = os.popen('type' + ' ' + filename + "| " + 'find /v /c""')
        output_num = log_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        log_num.close()
    elif operation_system == 'Linux':
        log_num = os.popen('cat' + filename + '| wc -l')
        output_num = log_num.readlines()
        final_num = str(output_num[0]).replace("\n",'')
        log_num.close()
    with open(filename,"r",encoding="utf-8") as f:
        reader = f.readlines()
        x = 0
        while x < int(final_num):
            action_result = str(reader[x]).split(" ")[3]
            user_result = str(reader[x]).split(" ")[0]
            time_result = str(reader[x]).split(" ")[12]
            package_result = str(reader[x]).split(" ")[5]  
            result_one = {
                'username' : user_result,
                'actions' : action_result,
                'time' : time_result,
                'package' : package_result
            }
            print(result_one)
            insert_result = collection_table.insert_one(result_one)
            print(insert_result)
            print(insert_result.inserted_id)
            x += 1



if __name__ == '__main__':
    c_t = str(datetime.datetime.now().strftime('%Y%m%d'))
    filename = "download_" + c_t + ".log"
    print(filename)
    db_port = int('XXX') # Your port number
    db_name = str(input('Plz input the database name:'))
    db_collection = str(input('Plz input the collection name:'))
    datafresh(filename,db_port,db_name,db_collection)
