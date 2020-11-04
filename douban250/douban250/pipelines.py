# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

# from scrapy.conf import settings  # 该导包方式已经不适用，解释可见博文：https://www.cnblogs.com/banshaohuan/p/11848264.html

from scrapy.utils.project import get_project_settings
import pymongo
class Douban250Pipeline:
    """
    # 写入json文件格式
    def __init__(self):
        self.f = open("douban250.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()
    """
    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # 创建mongodb连接
        client = pymongo.MongoClient(host=host,port=port)
        db = client[dbname]
        # 获取存放电影数据的表名
        self.port = db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        # 向表里插入数据
        self.port.insert(data)
        return item