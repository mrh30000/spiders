"""
[课程内容]: Python采集douyu舞蹈视频

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm

"""

import requests
import re
url = 'https://v.douyu.com/api/stream/getStreamUrl'
data = {
    'v': '220320220627',
    'did': '10000000000000000000000000001501',
    'tt': '1656318502',
    'sign': 'f0194e25c25283cbd53ef52c0acf45f8',
    'vid': 'kDe0W29DOwaMA4Bz',
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}

response = requests.post(url=url, data=data, headers=headers)
print(response.json())
m3u8_url = response.json()['data']['thumb_video']['high']['url']
print(m3u8_url)
m3u8_data = requests.get(url=m3u8_url, headers=headers).text

m3u8_data = re.sub('#E.*', '', m3u8_data).split()
for ts in m3u8_data:
    ts_url = 'https://play-tx-ugcpub.douyucdn2.cn/live/high_33282775320220508200007-upload-d9f8/' + ts
    ts_content = requests.get(url=ts_url, headers=headers).content
    with open('【奶优米呀】05-07 本场人气值TOP2舞蹈.mp4', mode='ab') as f:
        f.write(ts_content)
    print(ts_url)

