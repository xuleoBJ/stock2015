import urllib.request
import os
from datetime import datetime
from bs4 import BeautifulSoup

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def getIfengNews():
    folder = makeTodayDirStr()
    url = 'http://www.ifeng.com/'
    print("-"*60)
    print(url)
    curHtlm = urllib.request.urlopen(url)
    soup = BeautifulSoup(curHtlm,"lxml")
    newsList = soup.find('u1', {"class":"FNewMTopLis"})
    print(newsList)
    for newsItem in newsList:
        newsLine = newsItem.get_text()
        if newsLine !="":
            print(newsLine)

def getSinaNews():
    folder = makeTodayDirStr()
    url = 'http://roll.news.sina.com.cn/s/channel.php?ch=01#col=97&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1 '
    print("-"*60)
    print(url)
    curHtlm = urllib.request.urlopen(url)
    soup = BeautifulSoup(curHtlm,"lxml")
    newsList = soup.find_all('a', {"target":"_blank"})
    #print(newsList)
    for newsItem in newsList:
        newsLine = newsItem.get_text()
        if newsLine !="":
            print(newsLine)
    
def makeTodayDirStr():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = "e:/webScrapy/"+strToday
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath


if __name__ == '__main__':
    getSinaNews()

