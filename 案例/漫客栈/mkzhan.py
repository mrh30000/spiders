import requests
from lxml import etree
import os
import asyncio
import aiohttp
async def task(session,url,title,j):
    async with session.get(url) as response:
        content = await response.content.read()
        with open('./{}/{}.jpg'.format(title,j),'wb') as f:
            f.write(content)

headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'referer': 'https://www.mkzhan.com/'
}
url = 'https://www.mkzhan.com/214990/'
d_url = 'https://comic.mkzcdn.com/chapter/content/v1/?chapter_id={chapterid}&comic_id=214990&format=1&quality=1&sign=3cde9e24a99e0d2e52e8e99be59fd7c5&type=1&uid=61087880'
reqs = requests.get(url).text
# print(reqs)
tree = etree.HTML(reqs)
r = tree.xpath('//div[@class="chapter__list clearfix"]/ul/li')[5:]
# print(r)
for i,li in enumerate(r):
    title = li.xpath('./a/text()')[-1].strip()
    chapterid = li.xpath('./a/@data-chapterid')[0]
    if not os.path.exists('./{}'.format(title)):
        os.mkdir('./{}'.format(title))
    # print(title,chapterid)
    new = d_url.format(chapterid=chapterid)
    # print(new)
    data = requests.get(url=new, headers=headers).json()['data']
    pages = data['page']
    async with aiohttp.ClientSession as session:
        tasks = [asyncio.create_task(task(session,page,title,j) for j,page in enumerate(pages))]
        await asyncio.wait(tasks)

    if i == 1:
        break


