import urllib.request
import os
from datetime import datetime

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]


def find_image(url):
    html = url_open(url).decode('utf-8')
    image_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a + 150)
        if b != -1:
            image_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=',b)
    for each in image_addrs:
        print(each)
    return image_addrs

def save_image(folder,image_addrs):
    for each in image_addrs:
        filename =os.path.join(folder, each.split('/')[-1])
        with open(filename,'wb') as f:
            each = "http:" + each
            img = url_open(each)
            f.write(img)
            
def makeTodayDirStr():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = "e:/webScrapy/"+strToday
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath

def download_girls(pages = 20):
    folder = makeTodayDirStr()
    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        image_addrs = find_image(page_url)
        save_image(folder,image_addrs)

if __name__ == '__main__':
    download_girls()
