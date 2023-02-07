# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs
import json

from itemadapter import ItemAdapter


class QqynproPipeline:
    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')
        self.file.write('{\n')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "," + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.write('}')
        self.file.close()
