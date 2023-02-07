"""
[课    题]: Python项目--链家房源数据爬取与分析可视化

*python基础入门，0基础学员听完即会哦！！！！！！

[授课老师]: 青灯教育-思语老师
[课程时间]: 20:05开始

[课程内容]:
    1.网络爬虫
    2.多页数据采集
    3.csv表格保存数据
    4.数据可视化
----------------------------------------------------------------------------------
课后的回放录播资料凭借直播结束前的直播签到，找助理老师领取
    包括:相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件
完成课程签到的同学将有机会领取今天的课程福利
--------------------------------------------------------------------------------------------
[环境使用]:
    python3.8 | Anaconda
    pycharm

[相关模块]:
    <第三方模块>
    requests   >>> pip install requests  1
    lxml
    pandas
    pyecharts
    <内置模块>
    csv

模块安装方法：win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名, 回车
--------------------------------------------------------------------------------------------
[听课建议]
    1. 基础比较薄弱的同学先听老师讲课，跟着老师的思路来，先听懂，课后找助理老师要录播
    2. 基础比较好的同学上课时，可以多帮助基础比较薄弱的同学，对自己而言稳固复习了，俗话说的好“温故而知新”，
        同时在听老师讲课的过程中也会学到新的知识点
    3. 对于本节课讲解的内容，看有什么不明白的地方可以直接在公屏上面提问， 具体哪行代码不清楚 具体那个操作不明白
    4. <早退>没有本堂课的资料
----------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

        - 失败三: cmd里面显示已经安装过了, 或者安装成功了, 但是在pycharm里面还是无法导入
            解决方法: 可能安装了多个python版本 (anaconda 或者 python 安装一个即可) 卸载一个就好
                    或者你pycharm里面python解释器没有设置好

        - 失败四: You should consider upgrading via the 'python -m pip insta11 --upgrade pip' comand.
                 表示pip版本过低，需要下载更高版本的 pip
            解决方法: 更新pip版本，更新命令为  python -m pip insta11 --upgrade pip，然后重新使用pip install 模块名 下载该模块
--------------------------------------------------------------------------------------------------
0基础  0
有基础  1
爬取数据基本流程：
一。分析数据来源
    明确数据：https://cs.lianjia.com/ershoufang/pg2/
    开发者工具    会 1 不会  2   F12 、右击检查
二。代码实现案例
1.发送请求，向网址发送请求
2.获取数据，获取源代码
3.解析数据，提取房源信息
4.保存数据，csv
"""
# 导入模块
import requests # 数据请求  第三方模块  需要下载  pip install requests
import lxml
from lxml import etree  # 解析模块
import csv
"""
1.发送请求，向网址发送请求
爬虫代码  -->浏览器 
"""
url = 'https://cs.lianjia.com/ershoufang/pg2/'
# 伪装
# requests headers
headers = {
    # 键值对
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# <Response [200]> 响应对象  200 状态码 成功
print(response)

"""
2.获取数据，获取源代码
"""
# .text  文本信息
# print(response.text)

"""
3.解析数据，提取房源信息
"""
et = etree.HTML(response.text)
# xpath 定位
"""
//  定位任意的标签
/   定位下一级标签
@   属性
[]  条件
"""
# 所有房源
doc = et.xpath('//*[@id="content"]/div[1]/ul/li')
# print(doc)

list_1 = []
# for 循环
for li in doc:
    # print(li)
    # 标题
    title = li.xpath('.//div[@class="title"]/a/text()')[0]
    # print(title)
    # 价格
    price = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')[0]
    # print(price)
    # 位置
    position = li.xpath('.//div[@class="positionInfo"]/a/text()')
    # print(position)
    # if 判断
    if position:
        position = '-'.join(position)
    # print(position)
    list_1.append([title, price, position])
print(list_1)
for p in list_1:
    print(p)
    with open('ershoufang1.csv', mode='a', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(p)

"""
爬虫：可见即可爬  文字 音频 视频 图片   
"""
""""
想学好python找工作  6  3-7个月
爬虫
数据分析
开发
项目开发：
关键字  31个

想学好python做兼职  9 1-3 个月
    小外包  200 -500
    中等外包  1000以上
    大外包：几千 - 1万
...
双十一优惠：8880
- 预定300抵扣2000学费 6880
    - 助学通道  分期  0利息0手续费  12  573.33
    两个小外包
- 课程赠送  两个课程  4680元
    - 人工智能
    - 自动化办公
- 腾讯课堂 抽奖 --》iphone 14 

"""