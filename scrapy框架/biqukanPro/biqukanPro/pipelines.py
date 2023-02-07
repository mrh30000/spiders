# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter

import scrapy
class BiqukanproPipeline:
    def process_item(self, item, spider):
        xs_link = 'https://www.bqkan8.com'
        xs_zjlist = item['xs_zjlist']
        # print(xs_link)
        if not os.path.exists('../bqkan'):
            os.mkdir('../bqkan')
        for zj in xs_zjlist:
            yield scrapy.Request(xs_link+zj, callback=self.parse_detail)

    def parse_detail(self, response):
        res = response.xpath('/html/body/div[@class="book reader"]/div[@class="content"]')[0]
        content = res.xpath('./div[@class="showtxt"]//text()').extract_first()
        name = res.xpath('./h1/text()').extract_first()
        with open('../bqkan'+name+'.txt',mode='w') as f:
            f.write(content)
        pass
