"""
[课程内容]: Python采集微博评论数据

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm

"""
import pprint
import re
import requests
import csv
import pandas as pd


# f = open('微博评论.csv', mode='a', encoding='utf-8', newline='')
# csv_writer = csv.DictWriter(f, fieldnames=[
#     '用户',
#     '地区',
#     '评论',
#     '日期',
# ])
# csv_writer.writeheader()


url = 'https://m.weibo.cn/comments/hotflow?id=4784937075214225&mid=4784937075214225&max_id_type=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)

lis = []
for index in response.json()['data']['data']:
    content = ''.join(re.findall('[\u4e00-\u9fa5]+', index['text']))
    dit = {
        '用户': index['user']['screen_name'],
        '地区': index['source'].replace('来自', ''),
        '评论': content,
        '日期': index['created_at']
    }
    lis.append(dit)
    # csv_writer.writerow(dit)
    print(dit)

pd_data = pd.DataFrame(lis)
pd_data.to_excel('微博评论.xlsx')