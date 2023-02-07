# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem

#需求：爬取sun网站中的编号，新闻标题，新闻内容，标号
class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=']

    #链接提取器：根据指定规则（allow="正则"）进行指定链接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')
    # link_detail = LinkExtractor(allow=r'question/\d+/\d+\.shtml')
    rules = (
        #规则解析器：将链接提取器提取到的链接进行指定规则（callback）的解析操作
        Rule(link, callback='parse_item', follow=False),
        #follow=True：可以将链接提取器 继续作用到 连接提取器提取到的链接 所对应的页面中
        Rule(LinkExtractor(allow=r'political/politics/index?id=\d+'),callback='parse_detail')
    )
    #http://wz.sun0769.com/html/question/201907/421001.shtml
    #http://wz.sun0769.com/html/question/201907/420987.shtml

    #解析新闻编号和新闻的标题
    #如下两个解析方法中是不可以实现请求传参！
    #如法将两个解析方法解析的数据存储到同一个item中，可以以此存储到两个item
    def parse_item(self, response):
        # print(response)
        #注意：xpath表达式中不可以出现tbody标签
        #/html/body/div[2]/div[3]/ul[2] /html/body/div[2]/div[3]/ul[2]
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        # link = 'https://wz.sun0769.com/'
        for tr in li_list:
            new_num = tr.xpath('./span[1]/text()').extract_first()
            new_title = tr.xpath('./span[3]/a/text()').extract_first()
        #     new_href = tr.xpath('./span[3]/a/@href').extract_first()
        #     # print(new_num,new_title,new_href)
            item = SunproItem()
            item['title'] = new_title
            item['new_num'] = new_num
        #     item['href'] = link + new_href
            yield item

    #解析新闻内容和新闻编号
    def parse_detail(self,response):
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract()
        new_content = ''.join(new_content)

        # print(new_id,new_content)
        item = DetailItem()
        item['content'] = new_content
        item['new_id'] = new_id

        yield item