class mirrors:
    def __init__(self,name):
        self.name = name

    @property
    def mirrorspools(self):
        from jmespath import search
        mirrors_pools = {"aliyun": [
    {"domain": "mirrors.aliyun.com","link":"http://mirrors.aliyun.com/pypi/simple/"}],
    "ustc":[
    {"domain":"pypi.mirrors.ustc.edu.cn","link": "https://pypi.mirrors.ustc.edu.cn/simple/"}],
    "douban":[
    {"domain":"pypi.douban.com","link": "http://pypi.douban.com/simple/"}],
    "tsinghua":[
    {"domain":"pypi.tuna.tsinghua.edu.cn","link": "https://pypi.tuna.tsinghua.edu.cn/simple/"}]
    }
        result = search(self.name,mirrors_pools)
        return result

