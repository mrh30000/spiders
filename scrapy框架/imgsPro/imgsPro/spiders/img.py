# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://699pic.com/tupian/kouzhao.html']
    rules = (
        # 规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
        Rule(LinkExtractor(allow=r'/soso/kouzhao-complex'), callback='process_request', follow=False),
        # follow=True：可以将链接提取器 继续作用到 连接提取器提取到的链接 所对应的页面中
        # Rule(LinkExtractor(allow=r'political/politics/index?id=\d+'), callback='parse_detail')
    )

    def process_request(self, links):
        print(links)
        # ret = []
        # for link in links:
        #     try:
        #         page = re.search('/soso/kouzhao-complex---------\d*--\d*', link.url).group()
        #         print(page)
        #         # type = re.search('type=\d+', link.url).group()
        #         link.url = 'https://699pic.com' + page
        #     except Exception:
        #         pass
            # ret.append(link)
        # return ret
    # def parse(self, response):
    #     # print(response.text)
    #     # //*[@id="wrapper"]/div[5]/div/div[1] /div[1]
    #     # /html/body/div[8]/div[5]
    #     # div_list = response.xpath('//*[@id="wrapper"]/div[@class="imgshow clearfix"]/div[@class="swipeboxEx"]/div')
    #     # print(div_list)
    #     div_list = response.xpath('/html/body/div[@id="wrapper"]/div[@class="imgshow clearfix"]/div[@class="swipeboxEx"]/div')
    #     # print(div_list)
    #     http = 'https:'
    #     for div in div_list:
    #         #注意：使用伪属性
    #         src = div.xpath('./a/img/@data-original').extract_first()
    #         # print(src)
    #         item = ImgsproItem()
    #         item['src'] = http + src
    #
    #         yield item
