# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : tbh5.py
# @Project  : PythonReversePath
import requests

cookies = {
    'cna': 'C6vqG7JR2h4CAa8AOExalk2+',
    'l': 'fBayfyOILWkrLhVGBO5CPurza779UIRb8sPzaNbMiIEGa6IFTFGLWNCFok0k7dtjgTfbmetrhWACFddLZ3UKNxDDBecuBKW9LxJ6-bpU-L5..',
    'tfstk': 'ck8CBraLGJ2B4buu-9GZT_ryKg7lZePfND6HOvhVeUWLTQRCiBUVhFt2q8QPw11..',
    'isg': 'BJqaMeDtrSiipyDvnOFwzTTq60C8yx6l_BE4i6QXGS34FztRjFuUtdQm4-OLx5Y9',
    '_m_h5_tk': 'da300df2b55022cae9f25c03373efea4_1673366240339',
    '_m_h5_tk_enc': '3087a463342100265433213db194767c',
}

headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'cna=C6vqG7JR2h4CAa8AOExalk2+; l=fBayfyOILWkrLhVGBO5CPurza779UIRb8sPzaNbMiIEGa6IFTFGLWNCFok0k7dtjgTfbmetrhWACFddLZ3UKNxDDBecuBKW9LxJ6-bpU-L5..; tfstk=ck8CBraLGJ2B4buu-9GZT_ryKg7lZePfND6HOvhVeUWLTQRCiBUVhFt2q8QPw11..; isg=BJqaMeDtrSiipyDvnOFwzTTq60C8yx6l_BE4i6QXGS34FztRjFuUtdQm4-OLx5Y9; _m_h5_tk=da300df2b55022cae9f25c03373efea4_1673366240339; _m_h5_tk_enc=3087a463342100265433213db194767c',
    'pragma': 'no-cache',
    'referer': 'https://h5.m.taobao.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.76',
}

params = {
    'jsv': '2.7.0',
    'appKey': '12574478',
    't': '1673355800381',  # 变化
    'sign': '738441739061fccd015122384c75f490',  # 变化  作业: Python调试js 执行得到sign
    'api': 'mtop.taobao.rate.detaillist.get',
    'v': '5.0',
    'ecode': '1',
    'type': 'jsonp',
    'timeout': '20000',
    'dataType': 'jsonp',
    'sessionOption': 'AutoLoginOnly',
    'jsonpIncPrefix': 'haloMtop',
    'callback': 'mtopjsonphaloMtop2',
    # 分页逻辑 pageno
    'data': '{"showTrueCount":false,"auctionNumId":"652797551998","rateType":"","searchImpr":"-8","expression":"","orderType":"","pageSize":10,"pageNo":1}',
}

response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.taobao.rate.detaillist.get/5.0/',
    params=params,
    cookies=cookies,
    headers=headers,
).text
print(response)
