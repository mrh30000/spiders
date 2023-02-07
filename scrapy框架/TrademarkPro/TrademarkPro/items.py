# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrademarkproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


#         item['zhucehao'] = info[i]['reg_num']
#         item['shenqingren'] = info[i]['reg_name']
#         item['shangping'] = info[i]['tm_name']
#         item['qihao'] = info[i]['ann_num']
class ShangbiaoItem(scrapy.Item):
    zhucehao = scrapy.Field()
    shenqingren = scrapy.Field()
    shangping = scrapy.Field()
    qihao = scrapy.Field()
    pass
