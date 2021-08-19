import requests
import asyncio
import aiohttp

book_id = '4355363008'
page_no = 1
url = f'https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid={book_id}&pageNum={page_no}&order=asc&site='
resp = requests.get(url)
resp = resp.json()
chapters = resp['data']['chapter']['chapterInfo']
for chapter in chapters:
    title = chapter['chapter_title']
    c_id = chapter['chapter_id']
    print('%s %s' % (title, c_id))

resp = requests.get('https://api.xumiaojx.com/index/?url=https://v.qq.com/x/cover/m441e3rjq9kwpsc/q00405d7n2v.html')
print(resp.text)
