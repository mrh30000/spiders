import feapder


class FirstSpider(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.baidu.com")

    def parse(self, request, response):
        print(response.text)


if __name__ == "__main__":
    FirstSpider().start()