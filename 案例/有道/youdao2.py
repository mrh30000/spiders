
from urllib import request
import urllib
import re

#构造请求头信息
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}#谷歌浏览器

#http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule 网页上的url
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

key="白金之星，世界"

#发送到web服务器的表单数据
formdata={
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"15880563488791",
"sign":"cc2c40d740538fc5edc0380891faef27",
"ts":"1588053583943",
"bv":"f9c86b1fdf2f53c1fefaef343285247b",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTlME"

}

#经过urlencode转码
data=urllib.parse.urlencode(formdata).encode(encoding='utf-8')

#如果Request()方法中的data参数有值,那么这个请求就是POST
#如果没有，就是GET
req=request.Request(url,data=data,headers=header)

response=request.urlopen(req).read().decode()

#print(response)

# "tgt":"Platinum stars, and the world"}]] 提取Platinum stars, and the world
pat=r'"tgt":"(.*?)"}]]' #字符串中有"",再用''括起来表示字符串

result=re.findall(pat,response)

print("翻译结果:"+result[0])