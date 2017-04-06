# -*- coding:utf-8 -*- 

import urllib.request
import os
from bs4 import BeautifulSoup

def parser_youtube_page(curHtlm):
    print('-'*10, 'Current dealing...'+curHtlm)
    goalFilePath = os.path.basename(curHtlm)+".txt"
    fileWrited=open(goalFilePath, 'w')
    soup = BeautifulSoup(open(curHtlm,encoding="utf-8").read(), 'lxml')
    print (soup.title)
    inforList = soup.find_all('div',{'class':'content-wrapper'})

    for item in inforList:
        child_herf = item.find("a")
        printLine = child_herf.attrs["title"]+"\t"+child_herf.attrs["href"]
        print(printLine) 
        fileWrited.write(printLine+"\n")
    fileWrited.close()
    
def parser_videoList(curHtlm):
    print('-'*10, 'Current dealing...'+ curHtlm)
    goalFilePath = os.path.basename(curHtlm).replace('.html','.txt')
    fileWrited=open(goalFilePath, 'w')
    soup = BeautifulSoup(open(curHtlm,encoding="utf-8").read(), 'lxml')
    print (soup.title)
    inforList = soup.find_all('tr',{'class':"pl-video yt-uix-tile "})

    for item in inforList:
        strPre = "https://www.youtube.com/watch?v="
        printLine =item.attrs["data-title"] +"\t"+ strPre+item.attrs["data-video-id"]
        print(printLine) 
        fileWrited.write(printLine+"\n")
    fileWrited.close()
if __name__ == '__main__':
    dirHtlm = "D:\\youtubeList"
    fileNames=os.listdir( dirHtlm )
    for itemHtml in fileNames:
        itemHtmlPath = os.path.join(dirHtlm,itemHtml)
        if os.path.isfile(itemHtmlPath):
            print(itemHtml)
            #parser_youtube_page(os.path.join(dirHtlm,curHtlm))
            parser_videoList(itemHtmlPath)

