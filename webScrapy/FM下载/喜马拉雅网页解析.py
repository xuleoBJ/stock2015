# -*- coding:utf-8 -*- 

import urllib.request
import os
from bs4 import BeautifulSoup

def parser_xmly_page(curHtlm):
    print('-'*10, 'Current dealing...'+curHtlm)
    goalFilePath = os.path.basename(curHtlm)+".txt"
    fileWrited=open(goalFilePath, 'w')
    soup = BeautifulSoup(open(curHtlm,encoding="utf-8").read(), 'lxml')
    print (soup.title)
    inforList = soup.find_all("ul")
    idsList =[]
    for item in inforList:
        if item.has_attr("sound_ids"):
            sound_idsLine = item["sound_ids"]
            print(sound_idsLine)
            fileWrited.write(sound_idsLine)
            idsList.extend(sound_idsLine.split(','))
        else:
            pass
        # child_herf = item.find("a")
        # printLine = child_herf.attrs["title"]+"\t"+child_herf.attrs["href"]
        # print(printLine) 
        # fileWrited.write(printLine+"\n")
    print(set(idsList))
    fileWrited.close()
    

if __name__ == '__main__':
    dirHtlm = "D:\\youtubeList"
    fileNames=os.listdir( dirHtlm )
    for itemHtml in fileNames:
        itemHtmlPath = os.path.join(dirHtlm,itemHtml)
        if os.path.isfile(itemHtmlPath):
            print(itemHtml)
            #parser_youtube_page(os.path.join(dirHtlm,curHtlm))dd
            parser_xmly_page(itemHtmlPath)

