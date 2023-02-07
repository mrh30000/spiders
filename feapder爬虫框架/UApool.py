from feapder.network.user_agent import get

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

    }

    for i in range(10):
        print(headers['User-Agent'])
        headers['User-Agent'] = get()