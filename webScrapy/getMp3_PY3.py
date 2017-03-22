__author__ = 'xuleo'
import urllib.request
import os
import re
from datetime import datetime

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    return response.read()

def get_page(url):
    html = url_open(url).decode('utf-8')
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>' #正则表达式寻找页面地址

    page = int(re.findall(pattern,html)[0])
    return page


def save_mp3(strUrl,folder):
        print (strUrl)
        curMp3 = url_open(i)
        with open(strUrl,'wb') as f:
            f.write(image)
            f.close()


def download_mp3(folder,strUrl):
    folder = makeTodayDirStr()
    save_mp3(strUrl,folder)

def makeTodayDirStr():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = "e:/webScrapy/"+strToday
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath


if __name__ == '__main__':
    download_mp3(folder,strUrl)
