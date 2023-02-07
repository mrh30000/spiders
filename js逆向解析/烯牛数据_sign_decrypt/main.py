import requests

cookies = {
    'btoken': 'FI4NLZ315OYK7GLAW73RVTDNRS53D790',
    'hy_data_2020_id': '185b5754cebbc0-022f0c94d93a54-7a575473-1395396-185b5754cec10e7',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22185b5754cebbc0-022f0c94d93a54-7a575473-1395396-185b5754cec10e7%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22185b5754cebbc0-022f0c94d93a54-7a575473-1395396-185b5754cec10e7%22%7D',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    # 'cookie': 'btoken=FI4NLZ315OYK7GLAW73RVTDNRS53D790; hy_data_2020_id=185b5754cebbc0-022f0c94d93a54-7a575473-1395396-185b5754cec10e7; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22185b5754cebbc0-022f0c94d93a54-7a575473-1395396-185b5754cec10e7%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22185b5754cebbc0-022f0c94d93a54-7a575473-1395396-185b5754cec10e7%22%7D',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52',
}

json_data = {
    'payload': 'LBc3V0I6ZGB5bXsxTCQnPRBuAgQVcDhbICcmb2x3AjI=',
    'sig': 'FCC4B7EA5867C7C82AE4CD3E1A7A979D',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
