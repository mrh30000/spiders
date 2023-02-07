import scrapy


class YjbysSpider(scrapy.Spider):
    name = 'yjbys'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.yjbys.com/shixi/shixibaogaofanwen/248080.html']

    def parse(self, response):
        list = response.xpath('//div[@class="main"]/div[1]/div/div[2]//p/text()').extract()#/html/body/div[2]/div[1]/div/div[2]
        for txt in list:
            print(txt)
        pass
