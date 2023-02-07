"""
[课程内容]: Python实现批量采集抖音视频

[授课老师]: 青灯教育-自游  [上课时间]: 20:05

[环境使用]:
    Python 3.8
    Pycharm

    谷歌浏览器
    谷歌驱动

[模块使用]:
    requests >>> pip install requests
    re
    json
    selenium >>> pip install selenium==3.141.0 <需要浏览器和浏览器驱动>

---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加落落老师微信
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找落落老师领取录播, 然后再写代码
    3. 不要早退, 课后签到领取福利代码以及课程录播
----------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源  SSL
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名
            pip install -i https://pypi.doubanio.com/simple/ selenium==3.141.0
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
零基础同学  0
有基础同学  1

听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找落落老师领取录播, 然后再写代码
    3. 不要早退, 课后签到领取福利代码以及课程录播

先采集一个视频内容 ---> 采集这个视频博主所有视频内容

如何实现爬虫案例: 流程思路 <通用模板>

一. 数据来源分析:
    1. 明确需求:
        采集那个网站上面什么数据内容 ---> 1. 视频标题  2. 视频播放链接
    2. 通过开发者工具进行抓包分析, 分析数据所在地方
        会用 1 不会 2
        - F12 或者 鼠标右键点击检查选择network  刷新网页 ---> 为了让本网页相关数据内容, 重新加载一遍
        - 找视频播放链接在什么地方 ---> 找media
        - 已知 视频播放链接 ---> 分析这个视频播放链接在什么可以得到
            通过搜索分析, 可以找到视频数据来源, 但是链接是转码了  <代码实现时候, 提取出来, 然后进行解码就可以了>

二. 代码实现步骤过程
    1. 发送请求, 模拟浏览器对于url地址发送请求
        https://www.douyin.com/video/7154259081103035688  <视频播放详情页>
    2. 获取数据, 获取服务器返回响应数据
        开发者工具里面 response
    3. 解析数据, 提取我们想要数据内容
        - 视频链接
        - 视频标题
    4. 保存数据, 把视频内容保存本地文件夹

有点懵: 很正常, 这个案例涉及很多基础知识点 如果你基础不牢, 知识点没有学过, 你听不懂很正常
    但是, 我每行代码 都会告诉大家是什么意思, 为什么这样写 写得到内容是什么样子

想从零基础入门开始学习, 实现就业工作或者兼职外包 ---> 选择系统课程
    从零基础入门到项目实战, 包含爬虫 数据分析 全栈开发 常用知识点都会教授

报班学习之后, 老师多对一教学

想要学好python ---> 9
    1. 就业工作 --> 8-15K左右   1
    跟着课程内容 --> 3-7个月可以工作就业
        爬虫工程师
        数据分析师
        全栈开发工程师

        开发经验: 是指你用python实现相关案例项目, 所积累经验 <看得就是简历案例项目>
            1. 课程内容教学项目案例
            2. 接外包 ---> 某些案例也可以当作开发经验

        工作经验: 是指你从事相关工作所积累经验
        工作经历: 是指你工作的所积累经验

    2. 接外包兼职赚钱    2
    跟着课程内容 --> 1-3个月可以接外包赚钱
        月收普通情况 1-3K左右

        你有外包渠道吗? 外包不懂, 你不会做的怎么办呢?

    对于VIP学员系统课程
        - 专门VIP接单群
        - 提供一些接单渠道
        - 提供外包问题解答

课程内容教学 从入门到项目实战 ---> 就业工作/ 接外包赚钱

想要跟着老师系统学习, 想要了解系统课程
    加婧琪老师微信: python1018
        - 可以免费领取课程大纲 学习路线图
        - 可以量身定制学习规划, 就业规划
        - 可以享有双十一预售优惠
    - 预定300 可以获取学费最高减免2000
    - 价值 2680元人工智能课程赠送
    - 价值 1680元自动化办公课程赠送
    - 外包指导 / 就业指导
    - 分期免息学习 每天一杯奶茶钱就可以跟着老师学习了....

核心编程 高级开发 爬虫实战 数据分析 全栈开发<前端+后端> 人工智能 自动化办公

核心编程 高级开发  基础 + 进阶  无论学那个方向, 用python做什么东西, 都是需要掌握的

对比系统课程教学, 公开课讲解的都是简单案例 ---> 跟着系统学习 五节基础课程 + 五节爬虫课程 就可以掌握 你就可以自己写出来

    爬虫: 采集数据/网页自动化操作/自动化脚本<自动发送弹幕/评论/点赞/答题/抢购商品/签到....>

"""
# 导入数据请求模块 第三方模块 需要在cmd里面或者pycharm终端里面进行安装 pip install requests
import requests
# 导入正则  内置模块 不需要安装
import re
# 导入json模块  内置模块 不需要安装
import json
# 导入格式化输出模块 内置模块 不需要安装
from pprint import pprint
"""
1. 发送请求, 模拟浏览器对于url地址发送请求
    - <Response [200]> 表示响应对象
        对于url地址 请求成功, 但是不代表你一定得到数据
    - 为什么没有得到我们想要数据内容
        当我们被服务器识别出来是爬虫程序的时候, 我可能得不到数据, 或者得到数据不是我们想要的

selenium 模拟人的行为去操作浏览器, 获取所有视频ID
定位元素获取视频播放页url地址

selenium ---> 浏览器驱动谷歌 ---> 浏览器谷歌
"""
# 自动化测试模块
from selenium import webdriver
# 导入时间模块
import time
# 1. 打开浏览器  实例化浏览器对象 driver 浏览器对象
driver = webdriver.Chrome()
# 2. 输入网址, 访问网站
driver.get('https://www.douyin.com/user/MS4wLjABAAAAkzRSrOuSsM4Z1Ricsddumx_aSvX0jmOPcQR2qTs3PEtImBD8BomLrqvtIOBKOL0P')
# 3. 滑动页面, 让网页加载所有视频内容 selenium 去执行js代码
def drop_down():
    """执行页面滚动的操作 自定义函数"""  # javascript
    for x in range(1, 30, 4):  # 1 3 5 7 9  在你不断的下拉过程中, 页面高度也会变的
        time.sleep(1)
        j = x / 9  # 1/9  3/9  5/9  9/9
        # document.documentElement.scrollTop  指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

# 调用函数 实现网页自动下滑操作
drop_down()
# 4. 通过元素定位 通过 css 选择器查找元素 所有li标签
lis = driver.find_elements_by_css_selector('.Eie04v01')
if lis:
    pass
else:
    lis = driver.find_elements_by_css_selector('.ECMy_Zdt')
# for循环遍历
for li in lis:
    try:
        time.sleep(1)
        # 通过 css 选择器查找元素 具体哪一个标签里的数据内容
        url = li.find_element_by_css_selector('a').get_attribute('href')
        print(url)
        # 确定请求url地址
        # url = 'https://www.douyin.com/video/7154259081103035688'
        # 伪装 模拟浏览器 --> headers 请求头 <开发者工具里面进行复制粘贴>
        headers = {
            # user-agent 用户代理 表示浏览器基本身份信息
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
        }
        # 发送请求
        response = requests.get(url=url, headers=headers)
        """
        2. 获取数据, 获取服务器返回响应数据
            开发者工具里面 response  ---> response.text
        3. 解析数据, 提取我们想要数据内容
            - 视频链接
            - 视频标题
            正则re提取数据内容 会用 1  不会 2
        
        调用re模块findall方法  --> 找到我们想要的数据内容
        re.findall('什么数据', '什么地方')
        从什么地方, 去找什么样的数据内容
        从 response.text 里面 去找  <title data-react-helmet="true">(.*?)</title> 其中(.*?) 这段是我们要的数据
        print(json_data)  --> 打印字典数据 返回一行数据内容
        pprint(json_data) --> 打印字典数据 返回多行数据内容 展开效果
        
        字典数据提取内容  会 1 不会 2
            键值对取值 ---> 根据冒号左边的内容[键], 提取冒号右边的内容[值]
        """
        # 提取标题
        title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text)[0]
        # 提取视频信息
        video_info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
        # 解码  <class 'str'> requests.utils.unquote 解码  requests.utils.quote 编码
        html_data = requests.utils.unquote(video_info)
        # 数据类型转换 转json字典数据  json 数据存储格式  在python字典数据类型
        json_data = json.loads(html_data)
        # json_data 字典类型 --> 提取视频链接
        video_url = 'https:' + json_data['32']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
        """
        4. 保存数据, 把视频内容保存本地文件夹
            - 对于视频链接发送请求, 获取数据的
                response.content 获取二进制数据内容
        """
        # 获取视频内容 --> 对于视频链接地址发送请求, 获取二进制数据内容
        video_content = requests.get(url=video_url, headers=headers).content
        # 'video\\'<文件夹> + title<文件名> + '.mp4'<文件后缀> mode='wb' 二进制写入保存
        with open('video\\' + title + '.mp4', mode='wb') as f:
            # 写入/保存数据
            f.write(video_content)
        print(title)
        print(video_url)
    except:
        pass




