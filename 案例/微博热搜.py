"""
[课程内容]: Python采集微博搜热数据内容

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm

"""
# 导入数据请求模块
import requests
# 导入数据解析模块
import parsel
# 导入csv模块
import csv
# 创建csv文件
f = open('热搜_1.csv', mode='a', encoding='utf-8', newline='')
# 配置文件
csv_writer = csv.DictWriter(f, fieldnames=['排名', '标题', '热度'])
# 写入表头
csv_writer.writeheader()
# 确定请求网址
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
# 请求头伪装
headers = {
    # cookie 用户信息, 常用于检测是否有登陆账号
    'cookie': 'SINAGLOBAL=2194576767444.1252.1653631662098; SCF=AiA45EKFxAjYrCvhqi2bTLe0SAqE_jpZS8q540XxtfT96xrpVe0sOCVGYlwY7lrntPfiWAOmkvvKlEWtj_oc-5A.; ALF=1658906433; SUB=_2A25PvSorDeRhGeBN4lUR8ynIzT6IHXVtQbZjrDV8PUJbkNANLWj9kW1NRBhBZS-CZts5oRPGeerWH6lIG8taTwTC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5DhuWWX_yprukdgcBeR.lc5NHD95Qce0.NeheNShqEWs4Dqcj_i--fiK.7iKn0i--NiKL2iKn7i--Xi-zRiKy2i--ciKn0i-z0i--fiKnpiKLh; UOR=,,www.baidu.com; PC_TOKEN=43bbb46706; _s_tentry=www.baidu.com; Apache=404171765342.58246.1658300174701; ULV=1658300174720:11:7:5:404171765342.58246.1658300174701:1658294552686',
    # user-agent 用户代理 表示浏览器基本身份标识
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# 获取响应的文本数据
print(response.text)
# 转数据类型
selector = parsel.Selector(response.text)
# 第一次提取 css选择器 获取所有标签数据内容
trs = selector.css('#pl_top_realtimehot tbody tr')
# 定义排序
num = 1
# for 循环遍历
for tr in trs:
    # 获取热搜标题
    title = tr.css('.td-02 a::text').get()
    # 获取热搜热度
    hot = tr.css('.td-02 span::text').get()
    # 创建字典保存数据
    dit = {
        '排名': num,
        '标题': title,
        '热度': hot
    }
    # 保存数据
    csv_writer.writerow(dit)
    print(dit)
    num += 1
