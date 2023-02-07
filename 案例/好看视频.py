"""
[课程内容]: Python采集某小视频网站数据

[授课老师]: 青灯教育-自游  [上课时间]: 14:35

[环境使用]:
    Python 3.8
    Pycharm

[模块使用]:
    requests >>> pip install requests

win + R 输入cmd 输入安装命令 pip install 模块名 如果出现爆红 可能是因为 网络连接超时 切换国内镜像源
先听一下歌 等一下后面进来的同学, 20:05 正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信: python10010
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找木子老师领取录播, 然后再写代码
    3. 不要进进出出, 早退不仅没有录播, 你还会思路中断
---------------------------------------------------------------------------------------------------
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

---------------------------------------------------------------------------------------------------
如何配置pycharm里面的python解释器?
    1. 选择file(文件) >>> setting(设置) >>> Project(项目) >>> python interpreter(python解释器)
    2. 点击齿轮, 选择add
    3. 添加python安装路径
---------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1. 选择file(文件) >>> setting(设置) >>> Plugins(插件)
    2. 点击 Marketplace  输入想要安装的插件名字 比如:翻译插件 输入 translation / 汉化插件 输入 Chinese
    3. 选择相应的插件点击 install(安装) 即可
    4. 安装成功之后 是会弹出 重启pycharm的选项 点击确定, 重启即可生效
---------------------------------------------------------------------------------------------------

1. 采集视频内容
2. 采集视频信息相关数据保存表格 csv / Excel

爬虫代码实现步骤:
    1. 发送请求, 对于刚刚分析得到url地址发送请求
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取我们想要数据内容
    4. 保存数据, 把相应的数据保存本地

数据登陆之后, 你都可以直接查看的, 我只是换了一种更加高效复制粘贴方法
用程序代替人为重复操作的工作...

"""
# 导入数据请求模块
import requests  # pip install requests  模块导入未使用灰色待机状态  (手机)
import pandas as pd  # pip install pandas
import csv

f = open('video.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '视频博主',
    '视频上传时间',
    '点赞量',
    '播放量',
    '评论量',
    '视频时长',
    '视频播放地址',
])
csv_writer.writeheader()  # 写入表头
page = 1
while True:
    if page > 10:
        break
    # 发送请求的网址 (相当于打电话的电话号码)
    url = 'https://haokan.baidu.com/web/video/feed?tab=dongman_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1648190135118'
    # headers 请求头 伪装python代码 模拟成浏览器去发送请求, 为了防止被反爬  (插电话卡)
    # user-agent 用户代理 表示浏览器基本身份标识
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    # 通过requests模块里面get请求方法对于url地址发送请求,并且携带上headers请求头伪装, 最后用自定义变量response接收返回数据
    response = requests.get(url=url, headers=headers)
    # <Response [200]> response响应对象 200 状态码表示请求成功  (相当于电话拨通了 有一个嘟嘟嘟声音)
    # response.json() 获取响应对象json字典数据 提取字典数据里面东西, 就可以键值对取值, 根据冒号左边的内容, 提取冒号右边的内容
    # python里面 [] list 列表数据  {} 字典数据类型或者集合 type() 查看数据类型
    videos = response.json()['data']['response']['videos']
    lis = []
    for video in videos:  # for循环遍历, 可以对于一个列表里面元素 进行一个一个提取
        play_url = video['play_url']  # 视频播放地址
        title = video['title']  # 视频标题
        comment = video['comment']  # 评论量
        duration = video['duration']  # 视频时长
        play_volume = video['fmplaycnt_2']  # 播放量
        like = video['like']  # 点赞量
        date = video['publish_time']  # 视频上传时间
        name = video['source_name']  # 视频博主
        dit = {
            '标题': title,
            '视频博主': name,
            '视频上传时间': date,
            '点赞量': like,
            '播放量': play_volume,
            '评论量': comment,
            '视频时长': duration,
            '视频播放地址': play_url,
        }
        # lis.append(dit)
        # video_content = requests.get(url=play_url, headers=headers).content
        # with open('video\\' + title + '.mp4', mode='wb') as f:
        #     f.write(video_content)

        csv_writer.writerow(dit)
        print(title, comment, duration, play_volume, like, date, name, play_url)
    page += 1


# pd_data = pd.DataFrame(lis)
# pd_data.to_excel('data.xls', index=False)
# pd_data.to_csv('data_1.csv', index=False)
