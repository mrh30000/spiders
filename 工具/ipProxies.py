import time
import requests
from lxml import etree


class DaiLi(object):
    def __init__(self):
        self.base_URL = 'https://www.kuaidaili.com/free/inha/{}/'
        # self.test_URL = 'http://httpbin.org/ip'
        self.test_URL = 'https://www.amazon.cn/gp/navigation/ajax/generic.html?ajaxTemplate=hamburgerMainContent&pageType=Gateway&hmDataAjaxHint=1&navDeviceType=desktop&isSmile=0&isPrime=0&isBackup=false&hashCustomerAndSessionId=c108bde04b677f19f2e5d7df74ff6ce0cad515fc&isExportMode=false&languageCode=zh_CN&environmentVFI=AmazonNavigationCards%2Fdevelopment%40B6099827072-AL2_x86_64&secondLayerTreeName=apparel_shoes%2Bcomputer_office%2Bhome_kitchen%2Bbeauty_pca%2Bkindle_ebook%2Bsports_outdoor%2Bgrocery%2Bbaby_toy%2Bphones_elec%2Bjewelry_watch%2Bhome_improvement%2Bvideo_game%2Bmusical_instrument%2Bcamera'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}
        self.base_xpath = '//div/div/table[@class="table table-bordered table-striped"]/tbody/tr'

    def get_response(self, url, proxies=None):
        try:
            response = requests.get(url=url, headers=self.headers, proxies=proxies)
            # time.sleep(0.5)
            return response.text
        except Exception as f:
            print('请求有误,错误为：%s' % f)

    def get_url(self, page):
        url = self.base_URL.format(page)
        return url

    def xpath_html(self, html):
        html1 = etree.HTML(html)
        datas = html1.xpath(self.base_xpath)
        DiZhi = []
        for i in datas:
            dizhi = {'IP': i.xpath('./td/text()')[0], 'DuanKou': i.xpath('./td/text()')[1]}
            DiZhi.append(dizhi)
        return DiZhi

    def save_data(self, data):
        IPS = []
        for i in data:
            proxies = {'http': 'http://' + i['IP'] + ':' + i['DuanKou']}
            try:
                print(proxies)
                response = requests.get(url=self.test_URL, headers=self.headers, proxies=proxies, timeout=2)

                if response.status_code == 200:
                    print(response.status_code)
                    print(response.text)
                    IPS.append(proxies)

            except Exception:
                print('超时链接')
        print(IPS)

    def run(self):
        for i in range(1, int(input('输入爬取页码')) + 1):
            url = self.get_url(i)
            html = self.get_response(url)
            data = self.xpath_html(html)
            self.save_data(data)


if __name__ == '__main__':
    dl = DaiLi()
    dl.run()