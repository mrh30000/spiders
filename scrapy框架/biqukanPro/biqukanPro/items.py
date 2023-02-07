# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqukanproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xs_type = scrapy.Field()
    xs_name = scrapy.Field()
    xs_link = scrapy.Field()
    xs_author = scrapy.Field()
    xs_zjlist = scrapy.Field()
    pass
