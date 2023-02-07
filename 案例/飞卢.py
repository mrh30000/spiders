"""
[课程内容]: Python采集飞卢小说内容

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm

[模块使用]:
    requests >>> 数据请求模块
    parsel >>> 数据解析模块
    pip install 模块名

多页 多个数据采集, 我们要去分析, 请求url地址变化规律
"""
import requests
import parsel
for page in range(1, 44):
    url = f'https://b.faloo.com/1163585_{page}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    selector = parsel.Selector(response.text)
    # css选择器, 就根据标签的属性提取数据
    title = selector.css('.c_l_title h1::text').get().replace('偷吃我外卖被辣哭，问我要索赔？   ', '')  # 获取一个标签内容 <第一个>  返回字符串
    content_list = selector.css('div.noveContent p::text').getall()  # 获取所有标签内容 返回数据列表
    content = '\n'.join(content_list)
    print(title)
    print(content)

    with open('偷吃我外卖被辣哭，问我要索赔？' + '.txt', mode='a', encoding='utf-8') as f:
        """
        标题 第一章xxx
        内容 xxxx
        标题 第二章 xxx
        内容 xxx
        """
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
