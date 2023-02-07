# !/usr/bin/nev python
# -*-coding:utf8-*-



import requests, os, jsonpath, re
from selenium import webdriver
from pprint import pprint
from lxml import etree


def main():

    start_url = r'https://pvp.qq.com/web201605/js/herolist.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',
        'Referer': 'https://pvp.qq.com/web201605/herolist.shtml'
    }

    driver = webdriver.Chrome(executable_path=r'D:pythonchromedriver.exe')

    # 第一次请求，获取hero_id hero_name hero_skin_names
    response = requests.get(start_url, headers=headers).json()
    # pprint(response)
    hero_ids = jsonpath.jsonpath(response, '$..ename')
    # pprint(hero_ids)
    hero_names = jsonpath.jsonpath(response, '$..cname')
    # pprint(hero_names)

    for hero_name, hero_id in zip(hero_names, hero_ids):
        hero_info_url = r'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(hero_id)


        # 发送英雄详情页请求得到 hero_info_content

        driver.get(hero_info_url)
        # 获取页面源码
        hero_info_content = driver.page_source
        # lxml解析
        hero_info_content_str = etree.HTML(hero_info_content)

        # 提取 hero_skin_names hero_skin_urls
        hero_skin_names = hero_info_content_str.xpath(r'//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[
            0].split('|')

        hero_skin_urls = hero_info_content_str.xpath(r'//ul[@class="pic-pf-list pic-pf-list3"]//img/@data-imgname')

        # hero_skin_name进行替换不必要的信息
        for hero_skin_name, hero_skin_url in zip(hero_skin_names, hero_skin_urls):
            suffix_notation = re.findall(r'&d.?', hero_skin_name)[0]
            hero_skin_name = hero_skin_name.replace(suffix_notation, '')
            # 补全hero_skin_url地址
            hero_skin_url = r'https:'+hero_skin_url
            # 获取图片的二进制信息
            img_content = requests.get(hero_skin_url, headers=headers).content
            try:
                # 创建文件夹
                if not os.path.exists('./{}'.format(hero_name)):
                    os.mkdir(r'./{}'.format(hero_name))
                with open(r'./{}/{}.jpg'.format(hero_name, hero_skin_name), 'wb')as f:
                    f.write(img_content)
                    print('图片正在下载：{}/{}.jpg'.format(hero_name, hero_skin_name))

            except Exception as e:
                continue


if __name__ == '__main__':
    main()
