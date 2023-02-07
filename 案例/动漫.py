"""
[课程内容]: Python采集动漫内容

[授课老师]: 青灯教育-自游

[环境使用]:
    Python 3.8
    Pycharm 2021.2版本

[模块使用]:
    import requests >>> pip install requests
    import re
    import os

爬虫案例基本流程思路:

一. 数据来源分析
    1. 确定自己需求:
        采集那个网站上面什么数据内容
        https://www.dongmanmanhua.cn/
    正常访问流程:
        1. 选中漫画 ---> 目录页面 <请求列表页面 获取所有章节链接>
        2. 选择一个漫画内容 ---> 漫画页面 <请求章节链接, 获取所有漫画内容url>
        3. 看漫画内容 <保存数据, 漫画图片内容保存下来>

    爬虫分析流程: <开发者工具进行抓包分析>
        1. 查看漫画图片url地址, 是什么样子
            https://cdn.dongmanmanhua.cn/166052717362315191169.jpg?x-oss-process=image/quality,q_90
        2. 分析url地址在哪里
            通过搜索功能 <开发者工具>  166052717362315191169
            https://www.dongmanmanhua.cn/BOY/moutianchengweimoshen/116-%E7%AC%AC43%E7%AB%A0-%E5%A2%9E%E5%8A%A0%E6%88%98%E6%96%97%E5%8A%9B%E5%90%A73/viewer?title_no=1519&episode_no=116

    - F12打开开发者工具, 进行刷新网页
    - 点击Img
    通过对比分析请求url地址变化 ---> 漫画内容都是来于章节链接里面

二. 代码实现步骤过程
    1. 发送请求 ---> 对于目录页面发送请求
    2. 获取数据 ---> 服务器返回响应数据 <网页源代码数据>
    3. 解析数据 ---> 提取想要章节链接 / 漫画名字 / 章节名字

    4. 发送请求 ---> 对于章节链接发送请求
    5. 获取数据 ---> 服务器返回响应数据 <网页源代码数据>
    6. 解析数据 ---> 提取想要图片链接

    7. 保存数据 ---> 保存到本地


"""
# 导入数据请求模块
import requests
# 导入正则模块
import re
# 导入文件操作模块
import os.path
import asyncio
import aiohttp




headers = {
        # referer 防盗链 告诉服务器请求url地址 是从哪里跳转过来
        'referer': 'https://www.dongmanmanhua.cn/',
        # User-Agent  浏览器基本身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }

def get_response(html_url):
    """
    def 自定义函数关键字
    get_response: 自定义函数名字

    爬虫发送请求:
        模拟浏览器对于url地址发送请求
    :param html_url: 自定义形式参数
    :return: 响应对象
    """
    # 请求头 headers 模拟浏览器 ---> 字典数据类型, 构建完整键值对 <伪装请求头可以复制粘贴>

    # 通过数据请求模块 去发送请求
    response = requests.get(url=html_url, headers=headers)
    # return 返回 ---> 在代码里面 调用 get_response  函数 这个函数, 会给我们返回 response 这个数据
    return response


def get_info(html_url):
    """
    获取章节链接 / 漫画名字 / 章节名字
    :param html_url:
    :return:
    """
    # 调用发送请求函数
    html_data = get_response(html_url).text
    # re正则提取数据
    name = re.findall("title_title: '(.*?)',", html_data)[0]  # 提取漫画名字
    chapter_url_list = re.findall('data-sc-name="PC_detail-page_related-title-list-item".*?href="(.*?)"', html_data, re.S)
    title_list = re.findall('<span class="subj"><span>(.*?)</span></span>', html_data)
    return name, chapter_url_list, title_list


def get_img_url(chapter_url):
    """
    获取漫画url地址
    :param chapter_url: 章节url地址
    :return:
    """
    # 调用发送请求函数
    chapter_data = get_response(chapter_url).text
    # re获取所有漫画图片内容
    img_url_list = re.findall('alt="image" class="_images _centerImg" data-url="(.*?)"', chapter_data)
    # 403 Forbidden 没有访问权限  ---> 通过代码得到数据 请求头里面加防盗链
    return img_url_list


async def fetch(session, url, name, title):
    # 自动创建文件夹
    file = f'img\\{name}\\'
    # 如果没有这个文件夹的话
    if not os.path.exists(file):
        # 自动创建文件夹
        os.makedirs(file)
    # 对于图片链接发送请求 获取二进制数据

    async with session.get(url, verify_ssl=False, headers=headers) as response:
        img_content = await response.content()
        # file + title  保存地方以及保存文件名 mode 保存方式
        with open(file + title, mode='wb') as f:
            # 写入数据
            f.write(img_content)
            print(name, title)

def save(name, title, img_url):
    """
    保存数据
    :param name: 漫画名
    :param title: 图片名
    :param img_url: 图片链接
    :return:
    """
    # 自动创建文件夹
    file = f'img\\{name}\\'
    # 如果没有这个文件夹的话
    if not os.path.exists(file):
        # 自动创建文件夹
        os.makedirs(file)
    # 对于图片链接发送请求 获取二进制数据
    img_content = get_response(img_url).content
    # file + title  保存地方以及保存文件名 mode 保存方式
    with open(file + title, mode='wb') as f:
        # 写入数据
        f.write(img_content)
    print(name, title)


def main(page):
    """
    主函数 整合上面所有内容
    :param page:
    :return:
    """
    # 目录页面
    link = f'https://www.dongmanmanhua.cn/BOY/moutianchengweimoshen/list?title_no=1519&page={page}'
    # 调用获取章节链接 / 漫画名字 / 章节名字 函数
    name, chapter_url_list, title_list = get_info(link)
    # for循环遍历 提取数据
    for chapter_url, chapter_title in zip(chapter_url_list, title_list):
        # 字符串拼接
        chapter_url = 'https:' + chapter_url
        # 获取漫画内容
        img_url_list = get_img_url(chapter_url)
        # for循环遍历 提取数据
        num = 1
        for img_url in img_url_list:
            title = chapter_title + str(num) + '.jpg'
            # 调用保存数据函数
            save(name, title, img_url)
            # 每次循环 +1
            num += 1
async def asymain(page):
    async with aiohttp.ClientSession() as session:
        # 目录页面
        link = f'https://www.dongmanmanhua.cn/BOY/moutianchengweimoshen/list?title_no=1519&page={page}'
        # 调用获取章节链接 / 漫画名字 / 章节名字 函数
        name, chapter_url_list, title_list = get_info(link)
        # for循环遍历 提取数据
        for chapter_url, chapter_title in zip(chapter_url_list, title_list):
            # 字符串拼接
            chapter_url = 'https:' + chapter_url
            # 获取漫画内容
            img_url_list = get_img_url(chapter_url)
            tasks = [asyncio.create_task(fetch(session=session, url=url,name=name ,title = chapter_title + str(i) + '.jpg')) for i,url in enumerate(img_url_list)]
            await asyncio.wait(tasks)


if __name__ == '__main__':
    # 函数入口, 当你代码被当作模块调用的时候, 下面的代码不执行
    # for page in range(1, 0, -1):
    asyncio.run(asymain(1))


