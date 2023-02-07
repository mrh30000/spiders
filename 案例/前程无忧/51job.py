import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'From-Domain': '51job_web',
    'Origin': 'https://we.51job.com',
    'Pragma': 'no-cache',
    'Referer': 'https://we.51job.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
    'account-id': '',
    'partner': 'www_baidu_com',
    'property': '%7B%22partner%22%3A%22www_baidu_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D030200%26keyword%3Dpython%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': '338df9f1a1e005806422f12be541e18338eff19c4b4c27bdceb1aceeaa76f606',# 加密
    'user-token': '',
    'uuid': '612ee220d41ab137c823239f01a74e04',
}

params = {
    'api_key': '51job',
    'timestamp': '',
    'keyword': 'python',
    'searchType': '2',
    'function': '',
    'industry': '',
    'jobArea': '030200',
    'jobArea2': '',
    'landmark': '',
    'metro': '',
    'salary': '',
    'workYear': '',
    'degree': '',
    'companyType': '',
    'companySize': '',
    'jobType': '',
    'issueDate': '',
    'sortType': '0',
    'pageNum': '1',
    'requestId': '',
    'pageSize': '50',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}

params['timestamp']
response = requests.get('https://cupid.51job.com/open/noauth/search-pc', params=params, headers=headers)

