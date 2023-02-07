import base64
import time
import zlib
import scrapy
from meituanPro.items import MeituanproItem
import json
class MeituanSpider(scrapy.Spider):
    name = 'meituan'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']


    # 重写start_requests方法
    def start_requests(self):

        # 浏览器用户代理
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'Referer': 'https://gz.meituan.com/meishi/',
            'cookie' : '_lxsdk_cuid=1824947cc0bc8-05196afa665732-26021a51-154ac4-1824947cc0bc8; client-id=50a2f1c3-87f3-45cf-88b3-85a9a7a7bada; mtcdn=K; ci=20; rvct=20%2C84; uuid=5da83c659f0c4bf9bb0e.1659147794.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=120002231.1659086903545.1659108894439.1659147794613.3; userTicket=YuTbztuUodCDTODCrQSUzkLTevFtFrwHykxhEggr; u=2980393086; n=Iwl702690353; lt=0Nf1l4Kw7AMtsXufb5ki-d2D-ogAAAAA_xIAAFj7pDzEhEZK-zITNtc1yBfMsne7OqVqPebtnxKzkpGCVUVJT0iXeh1uSxH3wVTayg; mt_c_token=0Nf1l4Kw7AMtsXufb5ki-d2D-ogAAAAA_xIAAFj7pDzEhEZK-zITNtc1yBfMsne7OqVqPebtnxKzkpGCVUVJT0iXeh1uSxH3wVTayg; token=0Nf1l4Kw7AMtsXufb5ki-d2D-ogAAAAA_xIAAFj7pDzEhEZK-zITNtc1yBfMsne7OqVqPebtnxKzkpGCVUVJT0iXeh1uSxH3wVTayg; token2=0Nf1l4Kw7AMtsXufb5ki-d2D-ogAAAAA_xIAAFj7pDzEhEZK-zITNtc1yBfMsne7OqVqPebtnxKzkpGCVUVJT0iXeh1uSxH3wVTayg; unc=Iwl702690353; _lxsdk=1824947cc0bc8-05196afa665732-26021a51-154ac4-1824947cc0bc8; firstTime=1659148292405; _hc.v=c20218f3-a233-d16b-159b-c1b9895f04de.1659148292; WEBDFPID=007wy4wz015w5z96z936u605w353z16y8175xu8w556979587zwu10vx-1659234692779-1659148292058MUUAQUIfd79fef3d01d5e9aadc18ccd4d0c95078831; lat=23.134147; lng=113.338837; _lxsdk_s=1824d2b8aec-97f-151-bd1%7C%7C1'
        }
        # 指定cookies
        url = 'https://gz.meituan.com/meishi/api/poi/getPoiList'

        def deToken(data):
            encodes = str(data).encode()
            compress = zlib.compress(encodes)
            b_encode = base64.b64encode(compress)
            e_sign = str(b_encode, encoding='utf-8')
            return e_sign

        parames = {
            'cityName': '广州',
            'cateId': 0,
            ' areaId': 0,
            'sort': '',
            'dinnerCountAttrId': '',
            'page': 1,
            'userId': 2980393086,
            'uuid': 'aa9112bbe248482faea2.1659086890.1.0.0',
            'platform': 1,
            'partner': 126,
            'originUrl': 'https://gz.meituan.com/meishi/',
            'riskLevel': 1,
            'optimusCode': 10,
        }
        def get_token(params):
            sign = deToken(params)
            ip = {
                "rId": 100900,
                "ver": "1.0.6",
                "ts": round(time.time() * 1000),
                "cts": round(time.time() * 1000) + 2000,
                "brVD": [
                    297,
                    829
                ],
                "brR": [
                    [
                        1494,
                        934
                    ],
                    [
                        1494,
                        934
                    ],
                    24,
                    24
                ],
                "bI": [
                    "https://gz.meituan.com/meishi/",
                    ""
                ],
                "mT": [],
                "kT": [],
                "aT": [],
                "tT": [],
                "aM": "",
                "sign": sign
            }
            return deToken(ip)

        for page in range(1,10):
            parames['page'] = page
            if '_token' in parames:
                parames.pop('_token')
            parames['_token'] = get_token(parames)
            yield scrapy.Request(url=url, headers=headers,params=parames,callback=self.parse_item)
    def parse_item(self, response):
        # item = {}
        response_data = json.loads(response.content)
        # data = response_data.get('data')
        poiInfos = response_data.get('data').get('poiInfos')
        href = 'https://gz.meituan.com/meishi/'
        for poiInfo in poiInfos:
            item = MeituanproItem()
            item['title'] = poiInfo['title']
            item['avgScore'] = poiInfo['avgScore']
            item['address'] = poiInfo['address']
            item['avgPrice'] = poiInfo['avgPrice']
            item['detail_url'] = href + ['poiId']
            yield item
        # return item
