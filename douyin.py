import requests
import re
import webbrowser


def douyinurl(url):
    ua = {
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    response = requests.get(url, headers=ua, allow_redirects=False)

    url = response.headers['Location']

    itemids = re.findall("video/(.*?)/\?", url)[0]

    url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + itemids

    response = requests.get(url, headers=ua)

    videovid = response.json()["item_list"][0]['video']['vid']

    url = "https://aweme.snssdk.com/aweme/v1/play/?video_id=" + videovid + "&ratio=720p&line=0"

    response = requests.get(url, headers=ua, allow_redirects=False)

    url = response.headers['Location']

    return url


if __name__ == '__main__':
    url = input('请输入抖音分享链接')
    t = douyinurl(url)
    webbrowser.open(t)