# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

#
# class MeituanproPipeline:
#     def process_item(self, item, spider):
#         return item
class mysqlPileLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='47.113.195.193',port=3306,user='root',password='123456',db='meituan',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into meituan values("%s",%s,"%s",%s,"%s")'
                                %(item["title"],item["avgScore"],item["address"],item["avgPrice"],item["detail_url"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()