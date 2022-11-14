# 文件处理器
from filehandler import filesdetails
# 镜像大师
from sourceholder import mirrors


files2 = filesdetails('Windows','requirements.txt')
print(files2.counter)
print(files2.readlines)


ali_result = mirrors('aliyun')
print(ali_result.mirrorspools)

