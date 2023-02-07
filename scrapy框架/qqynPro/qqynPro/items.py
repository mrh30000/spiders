# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QqynproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    zone = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    company = scrapy.Field()
    pass
