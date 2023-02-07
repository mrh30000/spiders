"""
课程内容： python爬取B站视频内容

授课老师： 青灯教育 - 自游

环境介绍：
    python 3.8
    pycharm
模块使用：
    requests
    re
    subprocess
需要本节课的资料, 或者有什么问题都可以加视频上方的学习交流群的

分析一下B站视频数据和音频数据来自于哪里

1. 获取B站视频网页源代码
2. 解析数据, 提取我们想要的视频标题 / cid / session
3. 把cid session 传入我们找到的playurl这个数据包里面
4. 获取json字典数据
5. 解析数据提供 音频url 视频 url
6. 保存数据
7. 合成视频 把音频 和 视频内容 合成到一起

本节课案例需要注意的点:
    1. 请求头需要加上防盗链 >>> 如果没有加防盗链 是获取不到音频数据 和 视频数据
    2. 需要安装 ffmpeg 这个软件 并且需要设置环境变量
    3. 视频标题里面的特殊字符  需要用正则表达式替换掉 并且 视频标题里面不能有空格

之后也会在腾讯课堂上面直播讲解 这节课内容

"""
import subprocess

import requests  # 数据请求模块  需要 pip install requests
import re  # 正则表达式
import pprint  # 格式化输出模块

headers = {
    'referer': 'https://www.bilibili.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}


def get_response(html_url):
    """发送请求函数"""
    response = requests.get(url=html_url, headers=headers)
    return response


def get_video_info(html_url):
    """获取视频标题 / CID / session"""
    response = get_response(html_url)
    cid = re.findall('"cid":(\d+),', response.text)[0]
    session = re.findall('"session":"(.*?)"', response.text)[0]
    title = re.findall('<h1 title="(.*?)" class="video-title">', response.text)[0].replace(' ', '')
    # print(cid, session, title)
    video_info = [cid, session, title]
    return video_info


def get_video_content(cid, session, bv_id):
    index_url = 'https://api.bilibili.com/x/player/playurl'
    data = {
        'cid': cid,
        'qn': '0',
        'type': '',
        'otype': 'json',
        'fourk': '1',
        'bvid': bv_id,
        'fnver': '0',
        'fnval': '976',
        'session': session,
    }
    json_data = requests.get(url=index_url, params=data, headers=headers).json()
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    # print(audio_url, video_url)
    # pprint.pprint(json_data)
    video_content = [audio_url, video_url]
    return video_content


def save(title, audio_url, video_url):
    """保存数据"""
    audio_content = get_response(audio_url).content
    video_content = get_response(video_url).content
    with open(title + '.mp3', mode='wb') as f:
        f.write(audio_content)
    with open(title + '.mp4', mode='wb') as f:
        f.write(video_content)
    print(title, '保存完成')


def merge_data(video_name):
    """数据的合并"""
    print('视频合成开始:', video_name)
    cmd = f"ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4"
    # print(cmd)
    subprocess.run(cmd, shell=True)
    print('视频合成结束:', video_name)


def main(bv_id):
    """主函数"""
    url = f'https://www.bilibili.com/video/{bv_id}'
    video_info = get_video_info(url)
    video_content = get_video_content(video_info[0], video_info[1], bv_id)
    save(video_info[2], video_content[0], video_content[1])
    merge_data(video_info[2])


# if __name__ == '__main__':
#     bv = input('请输入你要下载的视频BV号: ')
#     # bv = 'BV1p4411d7og'
#     main(bv)

# url = 'https://www.bilibili.com/video/BV1p4411d7og'
# get_video_info(url)
main("BV1ET411y7Hk")