# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dl_name = scrapy.Field()
    dl_link = scrapy.Field()
    pass
