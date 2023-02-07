import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
# from tencentPro.items import RecruitItem
class TencentSpider(CrawlSpider):
    name = 'tencent'
    # allowed_domains = ['www.xxxx.com']
    start_urls = ["https://careers.tencent.com/search.html"]

    # rules = (
    #     Rule(LinkExtractor(allow=r'?index=\d+'), callback='parse_item', follow=True),
    # )
    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='D:\BaiduNetdiskDownload\chromedriver')
    def parse_item(trf, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # print(response)
        tr_list = response.xpath('//*[@class="recruit-list"]')#
        # print(tr_list)
        for tr in tr_list:
            title = tr.xpath('./a/h4/text()').extract()[0]
            #//*[@id="1476137841103740928"]//*[@id="1476137841103740928"]
            detailLink = tr.xpath('./div[1]/div/div/div[3]/@href').extract()[0]
            text = tr.xpath('./a/p[2]/text()').extract()[0]
            print(title,detailLink,text)
        # for tr in tr_list:
        #     new_num = tr.xpath('./td[1]/text()').extract_first()
        #     new_title = tr.xpath('./td[2]/a[2]/@title').extract_first()
        #     item = RecruitItem()
        #     item['title'] = new_title
        #     item['new_num'] = new_num
        #
        #     yield item
        # return item
    def closed(self,spider):
        self.bro.quit()
