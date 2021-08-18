import requests
import re
import csv
import threading

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

def spiderDouban():
    csv_writer = csv.writer(open('data/douban.csv', 'w', encoding='utf-8'))

    url = 'https://movie.douban.com/top250'
    resp = requests.get(url, headers = header)
    # print(resp.text)
    content = resp.text

    pattern = re.compile(r'<li>.*?<div class="info">.*?<div class="info">.*?'
                         r'<a href="(?P<href>.*?)".*?<span class="title">(?P<movie>.*?)</span>'
                         r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)

    movies = []
    result = pattern.finditer(content)
    for it in result:
        print('%s[%s]  %s' % (it['movie'], it['score'], it['href']))
        # print(it.groupdict())

        data = it.groupdict()
        movie_url = it['href']
        desc = load_movie(movie_url)
        data['desc'] = desc

        movies.append(data)
        csv_writer.writerow(list(data.values()))

    print('all end...')


def load_movie(url):
    resp = requests.get(url, headers=header)
    # print(resp.text)
    content = resp.text

    pattern = re.compile(r'<div class="related-info".*?<div class="indent" id="link-report">.*?<span property="v:summary" class="">(?P<desc>.*?)</span>', re.S)
    result = pattern.search(content)
    if result is not None:
        desc = result['desc'].strip().replace('<br />', '').replace(r'[\s| ]', '')
        print('load movie end...')
    else:
        desc = ''
    return desc


if __name__ == '__main__':
    spiderDouban()


