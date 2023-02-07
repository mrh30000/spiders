import requests
url = "http://127.0.0.1:3000/get_num"
data = {'a':1,'b':2}
req = requests.post(url,data)
print(req.text)
