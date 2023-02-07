# 导入数据请求模块 <工具>  需要安装 pip install requests  <没有安装 1 安装 0>
import requests
# 导入格式化输出模块 内置模块
from pprint import pprint
# 导入csv模块 内置模块
import csv
# 导入正则模块  内置模块
import re
 
 
def get_shop(index_url):
    """
    自定义获取详情页信息
    :param index_url: 详情页链接
    :return:
    """
    headers = {
        'Host': 'www.meituan.com',
        'Referer': 'https://chs.meituan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    }
    html_data = requests.get(url=index_url, headers=headers).text
    address, phone, openTime = re.findall('"address":"(.*?)","phone":"(.*?)","openTime":"(.*?)",', html_data)[0]
    return address, phone, openTime
 
 
# 创建文件
f = open('烤肉_1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '店名',
    '商圈',
    '评分',
    '评论',
    '人均',
    '地址',
    '电话',
    '营业时间',
    '最低',
    '经度',
    '纬度',
    '详情页',
])
# 写入表头
csv_writer.writeheader()
"""
发送请求: 模拟浏览器对于url地址发送请求
    - 请求链接过长, 可以分段写入
        1. 问号前面: 链接
        2. 问号后面: 请求参数/查询参数
    - 批量替换
        1. 选中内容, ctrl + R 选 .*
        2. 通过正则命令匹配数据 进行批量替换
            (.*?): (.*)
            '$1': '$2',
 
    - <Response [403]> 整体表示 响应对象 Response 响应 尖括号表示对象
        403 状态码 表示你没有访问权限  不知道你请求url地址是怎么来的,  ---> 告诉他你哪里来的
        <Response [200]>
        200 状态码 表示请求成功
 
    - 当你请求数据之后, 发现没有请求成功
        1. 被封IP了
        2. 请求头, 伪装不够好
 
"""
# 请求url
url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/70'
# 请求参数 --> 字典数据类型, 构建完整键值对
data = {
    'uuid': '33f2c67295cf4ddd94a2.1666955165.1.0.0',
    'userid': '266252179',
    'limit': '32',
    'offset': '32',
    'cateId': '-1',
    'q': '烤肉',
    'token': '7NdsKvHQcowCdRbBjsm8RDdeeeEAAAAAoRQAADxA4ujZplkBT2CqWCkPIeFmvjB3piQTL4CSZr4FKlP5EBYly-qlOiWnYuaHdDyAkA',
}
# 模拟浏览器 headers 请求头  了解 1 不了解 2
headers = {
    # Referer 防盗链, 告诉服务器请求url地址是从哪来跳转过来
    'Referer': 'https://chs.meituan.com/',
    # User-Agent 用户代理, 表示浏览器基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, params=data, headers=headers)
"""
获取数据: 获取服务器返回响应数据
    开发者工具 --> response  形式:有花括号的形式
    response.json() 获取响应json字典数据
 
解析数据: 提取我们想要数据信息
    店铺基本数据: 店名/评论 价格 经纬度....
 
    response.json() 获取响应json字典数据
 
字典取值: 键值对取值 --> 根据冒号左边的内容[键], 提取冒号右边的内容[值]
 
print(index)    打印字典数据, 呈现一行
pprint(index)   打印字典数据, 呈现多行, 展开效果 更加方便取值
"""
# for循环遍历, 把列表里面元素 一个一个提取出来  index自定义变量名<字典数据类型> 用于接收列表里面元素的
for index in response.json()['data']['searchResult']:
    # 详情页  字符串格式化方法 把 index["id"] 传入到字符串当中
    link = f'https://www.meituan.com/meishi/{index["id"]}/'
    # 调用获取基本信息函数
    address, phone, openTime = get_shop(link)
    # 创建一个字典
    dit = {
        '店名': index['title'],
        '商圈': index['areaname'],
        '评分': index['avgscore'],
        '评论': index['comments'],
        '人均': index['avgprice'],
        '地址': address,
        '电话': phone,
        '营业时间': openTime,
        '最低': index['lowestprice'],
        '经度': index['longitude'],
        '纬度': index['latitude'],
        '详情页': link,
    }
 
    # 写入/保存数据
    csv_writer.writerow(dit)
    print(dit)