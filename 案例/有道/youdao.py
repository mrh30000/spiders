import requests
import time
import math
import hashlib


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1660825449.9171424; OUTFOX_SEARCH_USER_ID="365024931@10.110.96.158"',
    'Origin': 'https://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'

}

data = {
    'i': 'aaa',
    'from': 'auto',
    'to': '',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': '',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': '',
    'keyfrom': 'fanyi.web',
}
ti = int(time.time() * 1000)
sign_a = f'client=fanyideskweb&mysticTime={ti}&product=webfanyi&key=fsdsogkndfokasodnaso'
data['mysticTime'] = str(ti)
data['sign'] = hashlib.md5(sign_a.encode('utf-8')).hexdigest()
response = requests.post('https://dict.youdao.com/webtranslate', headers=headers, data=data).text
print(response)