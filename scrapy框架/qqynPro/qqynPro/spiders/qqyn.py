import scrapy

from qqynPro.items import QqynproItem
class QqynSpider(scrapy.Spider):
    name = 'qqyn'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://baike.baidu.com/item/青春有你第三季/51140980?fr=aladdin']

    def parse(self, response):
        #/html/body/div[3]/div[4]/div/div[1]/div[1]/table[16]/tbody
        person_list = response.xpath('//div[@class="main_tab main_tab-defaultTab  curTab"]/table[16]//tr')
        # print(person_list)
        for person in person_list:
            item = QqynproItem()
            item['name'] = person.xpath('./td[1]/div/a/text()').extract_first()
            item['zone'] = person.xpath('./td[2]/div/text()').extract_first()
            item['height'] = person.xpath('./td[3]/div/text()').extract_first()
            item['weight'] = person.xpath('./td[4]/div/text()').extract_first()
            item['company'] = person.xpath('./td[5]/div/text()').extract_first()
            # print(name,zone,weight,height,company)
            yield item