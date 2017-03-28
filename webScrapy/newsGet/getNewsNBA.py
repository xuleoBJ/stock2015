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

def getEspnNBA():
    folder = makeTodayDirStr()
    url = 'http://www.espn.com/nba/'
    curHtlm = urllib.request.urlopen(url)
    soup = BeautifulSoup(curHtlm,"lxml")
    newsList = soup.find_all('a', {"data-mptype":"headline"})
    print("-"*60)
    print(url)
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

def getYahooNBA():
    folder = makeTodayDirStr()
    url = 'http://sports.yahoo.com/nba/'
    curHtlm = urllib.request.urlopen(url)
    soup = BeautifulSoup(curHtlm,"lxml")
    newsList = soup.find_all('h3')
    print("-"*60)
    print(url)
    for newsItem in newsList:
        newsLine = newsItem.get_text()
        if newsLine !="":
            print(newsLine)

if __name__ == '__main__':
    getEspnNBA()
    getYahooNBA()
