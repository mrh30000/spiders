# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanproItem(scrapy.Item):
    title = scrapy.Field()
    avgScore = scrapy.Field()
    address = scrapy.Field()
    avgPrice = scrapy.Field()
    detail_url = scrapy.Field()
    pass