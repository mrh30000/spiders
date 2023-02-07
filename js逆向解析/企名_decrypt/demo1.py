# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : PythonReversePath
import requests
import execjs  # pip install pyexecjs2


url = 'https://vipapi.qimingpian.cn/DataList/productListVip'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.qimingpian.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
}

# post请求  表单
data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid': '',
}

response = requests.post(url, headers=headers, data=data).json()
encrypt_data = response['encrypt_data']  # 通过键提取值
jscode = open('./demo1.js', 'r', encoding='utf-8').read()
# 执行js
ctx = execjs.compile(jscode).call('s', encrypt_data)
print(ctx)
