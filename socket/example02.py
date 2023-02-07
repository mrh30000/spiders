import socket

url = 'www.baidu.com'

port = 80

def blocking():
    sock = socket.socket()
    sock.connect((url, port))
    request_url = 'Get / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'
    sock.send(request_url.encode())
    response = b''
    chunk = sock.recv(1024)
    while chunk:
        response += chunk
        chunk = sock.recv(1024)
    print(response)

if __name__ == '__main__':
    blocking()
