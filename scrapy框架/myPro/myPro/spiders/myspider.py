# -*- coding: utf-8 -*-
import scrapy
from myPro.items import MyproItem


class MySpider(scrapy.Spider):
    name = 'myspider'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://lol.qq.com/main.shtml']

    # url = 'https://www.zhipin.com/c101010100/?query=python&page=%d'
    # page_num = 2

    # 回调函数接受item
    def parse_detail(self, response):
        item = response.meta['item']
        # /html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div  //*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div
        job_desc = response.xpath('/html/body/div[3]/div/div[2]/div//div')
        print(job_desc)
        for i in range(3):
            dl_div = job_desc[i]
            # print(dl_div,type(dl_div))
            a = dl_div.xpath('./ul/li/a | ./a')[0]#/html/body/div[3]/div/div[2]/div/div[1]/ul/li/a

            # item['dl_link'] = a.xpath('./@href').extract_first()
            # item['dl_name'] = a.xpath('./strong/text()').extract_first()
            print(a.xpath('./@href').extract_first())
            print(a.xpath('./strong/text()').extract_first())


        # yield item


    def parse(self, response):
        # print(response)
        # response.selector.remove_namespaces()
        li_list = response.xpath('/html/body/div[3]/div[1]/div[4]/ul/li[1]/a/@href').extract_first()
        detail_url = 'https://lol.qq.com/' + li_list
        item = MyproItem()
        yield  scrapy.Request(detail_url,callback=self.parse_detail,meta={'item': item})


