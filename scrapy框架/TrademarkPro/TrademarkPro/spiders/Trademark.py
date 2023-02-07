import json

import scrapy
from ..items import ShangbiaoItem

class TrademarkSpider(scrapy.Spider):
    name = 'Trademark'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']

    def start_requests(self):
        for i in range(1682, 0, -1):
            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'UM_distinctid=16eac05d31a122-071a188af83977-32365f08-100200-16eac05d3232e2;tmas_cookie=51947.7681.15402.0000',
                'Host': 'wsgg.sbj.cnipa.gov.cn:9080',
                'Origin': 'http://wsgg.sbj.cnipa.gov.cn:9080',
                'Referer': 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }
            data = {
                'page': '1',
                'rows': '2000000',
                'annNum': str(i),
                'annType': '',
                'tmType': '',
                'coowner': '',
                'recUserName': '',
                'allowUserName': '',
                'byAllowUserName': '',
                'appId': '',
                'appIdZhiquan': '',
                'bfchangedAgengedName': '',
                'changeLastName': '',
                'transferUserName': '',
                'acceptUserName': '',
                'regName': '',
                'tmName': '',
                'intCls': '1',
                'fileType': '',
                'totalYOrN': 'true',
                'appDateBegin': '',
                'appDateEnd': '',
                'agentName': '',
            }
            url = 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html'
            yield scrapy.FormRequest(url, formdata=data, headers=headers)
    def parse(self, response):
        res = json.loads(response.text)
        # print(res['rows'])
        info = res['rows']
        if info:
            for i in range(len(info)):
                # print(i)
                # print(info[i])
                item = ShangbiaoItem()
                item['zhucehao'] = info[i]['reg_num']
                item['shenqingren'] = info[i]['reg_name']
                item['shangping'] = info[i]['tm_name']
                item['qihao'] = info[i]['ann_num']
                yield item
