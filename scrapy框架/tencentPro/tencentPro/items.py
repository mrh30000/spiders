# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class RecruitItem(scrapy.Item):
    title = scrapy.Field()
    detailLink = scrapy.Field()
    text = scrapy.Field()