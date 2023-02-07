import requests
from feapder.network.user_agent import get

def Test():
    url = 'https://www.amazon.cn/gp/navigation/ajax/generic.html?ajaxTemplate=hamburgerMainContent&pageType=Gateway&hmDataAjaxHint=1&navDeviceType=desktop&isSmile=0&isPrime=0&isBackup=false&hashCustomerAndSessionId=c108bde04b677f19f2e5d7df74ff6ce0cad515fc&isExportMode=false&languageCode=zh_CN&environmentVFI=AmazonNavigationCards%2Fdevelopment%40B6099827072-AL2_x86_64&secondLayerTreeName=apparel_shoes%2Bcomputer_office%2Bhome_kitchen%2Bbeauty_pca%2Bkindle_ebook%2Bsports_outdoor%2Bgrocery%2Bbaby_toy%2Bphones_elec%2Bjewelry_watch%2Bhome_improvement%2Bvideo_game%2Bmusical_instrument%2Bcamera'
    proxies = [{'http': 'http://222.74.73.202:42055'},{'http': 'http://117.114.149.66:55443'}]
    headers = {}
    headers['User-Agent'] = get()
    for i in proxies:
        headers['User-Agent'] = get()
        response = requests.get(url=url,headers=headers,proxies=i,timeout=3)
        if response.status_code == 200:
            print('请求成功！')
        else:
            raise IOError('请求失败')
if __name__ == '__main__':
    # Test()
    import pymysql

    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='demo')
    db.close()