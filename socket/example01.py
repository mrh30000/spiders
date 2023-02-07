#搜狗图片 下载一张
import socket
import re
#搜狗图片
img_url="https://i02piccdn.sogoucdn.com/a3ffebbb779e0baf"

'''  拓展：如何使用HTTPS请求
#HTTPS请求
import ssl
client = ssl.wrap_socket(socket.socket())   #ssl.wrap_socket 一个装饰器
client.connect(('i02piccdn.sogoucdn.com',443))
'''

client = socket.socket()
# 创建连接              注意上面我们爬的是https协议的url，但是我们使用http也行的原因是自动进行了重定向
client.connect(("i02piccdn.sogoucdn.com",80))     #连接服务器，ip地址的映射可以定位到它的服务器

# 构造请求报文
data = "GET /a3ffebbb779e0baf HTTP/1.1\r\nHost:i02piccdn.sogoucdn.com\r\n\r\n"

# 发送数据
client.send(data.encode())   #报文要以字节码的形式

# 接收数据
first_data = client.recv(1024)
print("first_data",first_data)

length = int(re.findall(b"Content-Length: (.*?)\r\n",first_data)[0]) #在列表里，所以加0; 响应的也是字节码形式，所以加b
print(length)   #内容长度

# 写这句的原因是在双\r\n后面可能有数据，也可能没有，如果有就直接拿到了
# .*是匹配除了\r\n换行符之外的，后面加个re.S,则也可以匹配\r\n换行符，变成无敌的了！
image_data = re.findall(b"From Inner Cluster \r\n\r\n(.*?)",first_data,re.S)
if image_data:
    image_data = image_data[0]
else:
    image_data = b""
print(image_data)
# 拼接拿到相应长度的数据
while True:
    temp = client.recv(1024)
    image_data += temp
    if len(image_data)>=length:
        break
# 4.断开连接
client.close()

# 写入文件
with open("girl.jpg","wb") as f:
    f.write(image_data)
