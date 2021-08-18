import requests
from concurrent.futures import ThreadPoolExecutor

def spider_pear_video(url):
    cont_id = url.split('_')[1]
    video_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}'

    header = {
        "Referer": url
    }
    resp = requests.get(video_url, headers=header)
    result = resp.json()

    # https://video.pearvideo.com/mp4/adshort/20210818/cont-1739234-13176484-094526_adpkg-ad_hd.mp4
    # https://video.pearvideo.com/mp4/adshort/20210818/1629266801939-13176484-094526_adpkg-ad_hd.mp4  src_url
    src_url = result['videoInfo']['videos']['srcUrl']
    system_time = result['systemTime']
    download_url = src_url.replace(system_time, f'cont-{cont_id}')
    print(download_url)

    with open(f'data/video_{cont_id}.mp4', mode='wb') as f:
        f.write(requests.get(download_url).content)
        print(f'下载video_{cont_id}完成...')


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        t.submit(spider_pear_video, 'https://www.pearvideo.com/video_1739193')
    print('程序结束...')
