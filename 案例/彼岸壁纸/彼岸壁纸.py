"""
[课程内容]: Python采集彼岸壁纸

[授课老师]: 青灯教育 - 自游

[环境使用]:
    Python 3.8 解释器
    Pycharm 编辑器

"""
import re
import requests

for page in range(3, 11):
    url = f'http://www.netbian.com/index_{page}.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    img_info = re.findall('<a href="(.*?)" title=".*?" target="_blank"><img src=".*?" alt="(.*?)" />', response.text)
    print(img_info)
    for link, title in img_info:
        link_url = 'http://www.netbian.com' + link
        response_1 = requests.get(url=link_url, headers=headers)
        response_1.encoding = response_1.apparent_encoding
        img_url = re.findall('target="_blank"><img src="(.*?)" alt=".*?"', response_1.text)[0]
        print(img_url)
        img_content = requests.get(url=img_url, headers=headers).content
        with open('img\\' + title + '.jpg', mode='wb') as f:
            f.write(img_content)


