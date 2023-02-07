import scrapy
from biqukanPro.items import BiqukanproItem

class BiqukanSpider(scrapy.Spider):
    name = 'biqukan'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.bqkan8.com/']

    def parse_detail(self, response):
        item = response.meta['item']
        # /html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div  //*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div
        href_list = response.xpath('/html/body/div[@class="listmain"]/dl//dd/a/@href').extract()
        item['xs_zjlist'] = href_list
        yield item
    def parse(self, response):
        # print(response.text)
        list = response.xpath('//div[@class="wrap"]/div[1]/div[2]/ul//li')
        # print(list)
        item = BiqukanproItem()
        li = list[0]
        item['xs_type'] = li.xpath('./span[@class="s1"]/text()').extract_first()
        item['xs_link'] = 'https://www.bqkan8.com' +li.xpath('./span[@class="s2"]/a/@href').extract_first()
        item['xs_name'] = li.xpath('./span[@class="s2"]/a/text()').extract_first()
        item['xs_author'] = li.xpath('./span[@class="s5"]/text()').extract_first()
        yield scrapy.Request(item['xs_link'], callback=self.parse_detail, meta={'item': item})
        # yield item
