"""
[课      题]：Python爬取豆瓣Top250电影数据

[主讲老师]: 青灯教育 - 自游老师

[课程亮点]
    1、动态数据抓包演示
    2、csv文件保存
    3、requests模块的使用
    4、parsel解析数据的使用
[环境介绍]：
    python 3.8
    pycharm

    requests >>> pip install requests
    parsel >>> pip install parsel
    csv
win + R 输入cmd 输入安装命令 pip install 模块名

加视频上方python学习交流群获取相应的学习资料

写代码代码基本步骤:
    1. 发送请求, 确定url地址 然后对其发送请求
    2. 获取数据, 获取服务器返回的响应数据内容
    3. 解析数据, 提取我们想要内容
    4. 保存数据
    5. 多页数据爬取

如果说大家有想要爬取的网站, 可以在视频下面评论留言

"""
import requests  # 数据请求模块 第三方模块 pip install requests
import parsel  # 数据解析模块 第三方模块 pip install parsel
import csv
import time # 时间模块
f = open('豆瓣Top250.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '导演',
    '演员',
    '电影年份',
    '拍摄国家',
    '电影类型',
    '电影评分',
    '评论人数',
    '电影简介',
])
csv_writer.writeheader()
num = 1
for page in range(0, 250, 25):
    print(f'正在爬取第{num}页数据内容')
    num += 1
    time.sleep(1)
    # 1. 发送请求, 确定url地址 然后对其发送请求
    url = f'https://movie.douban.com/top250?start={page}&filter='
    # User-Agent 浏览器的基本标识 基本信息 headers请求头 主要是把python代码进行伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    #  2. 获取数据, 获取服务器返回的响应数据内容
    # print(response.text) # response.text 获取响应体的文本数据 字符串数据类型  >>> re正则表达式
    # 3. 解析数据, 提取我们想要内容
    # 解析数据方法: re正则表达式 / xpath / css选择器
    # parsel解析模块里面css选择器
    # 把获取到的html字符串数据类型进行转换
    selector = parsel.Selector(response.text)
    # css选择器 主要根据标签属性内容提取数据
    lis = selector.css('.grid_view li')  # 获取所有li标签 返回的数据 列表, 列表里面没一个元素都是selector对象
    for li in lis:
        title = li.css('.info .hd span.title:nth-child(1)::text').get()  # 电影的名字
        movie_info_list = li.css('.bd p:nth-child(1)::text').getall()  # 电影的信息
        # getall 返回的是列表 strip() 去除字符串左右两端空格
        actor_list = movie_info_list[0].strip().split('   ')
        if len(actor_list) > 1:
            actor_1 = actor_list[0].replace('导演: ', '')  # 导演
            actor_2 = actor_list[1].replace('主演: ', '').replace('/...', '')  # 主演
            movie_info = movie_info_list[1].strip().split(' / ')
            movie_year = movie_info[0]  # 电影的年份
            movie_country = movie_info[1]  # 电影的国家
            movie_type = movie_info[2]  # 电影的类型
            movie_sum = li.css('.inq::text').get()  # 电影简介
            movie_num = li.css('.rating_num::text').get()  # 电影评分
            comment = li.css('.star span:nth-child(4)::text').get().replace('人评价', '')  # 评论人数
        else:
            actor_1 = actor_list[0]
            actor_2 = 'None'
        dit = {
            '标题': title,
            '导演': actor_1,
            '演员': actor_2,
            '电影年份': movie_year,
            '拍摄国家': movie_country,
            '电影类型': movie_type,
            '电影评分': movie_num,
            '评论人数': comment,
            '电影简介': movie_sum,
        }
        csv_writer.writerow(dit)
        print(title, actor_1, actor_2, movie_year, movie_country, movie_type, movie_sum, movie_num, comment, sep='|')
