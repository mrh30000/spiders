import base64
import urllib
import requests

API_KEY = "mqBoUsy2TB6RAauQy6QpsGKb"
SECRET_KEY = "KMNENNDXaoiqMlddGDazyPTPVyb9o8Qd"


def main():
    # url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\IMG_20230121_210825.jpg",True) 方法获取
    payload = "type=anime&image={}".format(get_file_content_as_base64('./IMG_20230121_210825.jpg'))
    print(payload)
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Accept': 'application/json'
    # }
    #
    # response = requests.request("POST", url, headers=headers, data=payload).json()
    # print(response)
    # with open('./img.jpg', 'wb') as fimg:
    #     fimg.write(base64.b64decode(response['image']))
    # print(response.text)


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
