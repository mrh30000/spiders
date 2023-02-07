# from fake_useragent import UserAgent
import requests
import re
import uuid
import tqdm
import time
headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39",  # 随机生成一个代理请求
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
           "Connection": "keep-alive"}

# img_re = re.compile('"thumbURL":"(.*?)"')
img_re = re.compile('"replaceUrl":.*?"ObjURL":"(.*?)".*?')
img_format = re.compile("f=(.*).*?w")
# url_prefix = 'https://gimg2.baidu.com/image_search/'
tmp_file_name = 'D:/data_label/cl/%s.jpeg'
def file_op(img):
    uuid_str = uuid.uuid4().hex
    # tmp_file_name = 'D:/data_label/cl/%s.jpg' % uuid_str
    with open(file=tmp_file_name % uuid_str, mode="wb") as file:
        try:
            file.write(img)
            # time.sleep(0.5)
        except:
            pass



def xhr_url(url_xhr, start_num=1, page=5):
    start_num = start_num * 30
    end_num = start_num + page*30
    with open('url.txt','w') as f:
        try:
            for page_num in tqdm.tqdm(range(start_num, end_num, 30)):
                resp = requests.get(url=url_xhr+str(page_num), headers=headers)
                if resp.status_code == 200:
                    img_url_list = img_re.findall(resp.text)  # 这是个列表形式
                    # print(img_url_list)
                    for img_url in img_url_list:
                        img_url = img_url.replace('\\/','/')
                        f.write(img_url+'\n')
                        # img_rsp = requests.get(url=img_url, headers=headers)
                        # file_op(img=img_rsp.content)
                else:
                    break
        except:
            pass
    print("内容已经全部爬取")


if __name__ == "__main__":
    org_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&word={text}&pn=".format(text=input("输入你想检索内容:"))
    xhr_url(url_xhr=org_url, start_num=int(input("开始页:")), page=int(input("所需爬取页数:")))
    # ''.replace()
