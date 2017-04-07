from html.parser import HTMLParser
import urllib.request
import json
import os
import sys
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime 

##更改ID然后运行

dirCurDownload ="大咖读书会"
urladdress ="http://www.ximalaya.com/69149360/album/6294413"

def get_ids(urladdress):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
   
    r = requests.get(urladdress,headers=headers)

    if r.status_code == 200:
        stringHtml = r.content
        soup = BeautifulSoup(stringHtml, 'lxml')
        inforList = soup.find_all("div")
        idsList =[]
        for item in inforList:
            if item.has_attr("sound_ids"):
                sound_idsLine = item["sound_ids"]
                return (sound_idsLine)
    else:
        return ""

def parse_downloadText(sound_ids):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    goalFilePath ="下载地址_"+dirCurDownload+"_"+sID+".txt"
    fileWrited=open(goalFilePath, 'w')
    try:
        starttime = datetime.now()
        for sound_id in sound_ids:

            urladdress = 'http://www.ximalaya.com/tracks/' + sound_id + '.json'  
            music_json = requests.get(urladdress,headers=headers).json()
            if 'title' in music_json.keys() and 'play_path_32' in music_json.keys():  
                line = music_json['title']+'\t'+music_json['play_path_32']
                print(line)
                fileWrited.write(line+"\n")
                

        endtime = datetime.now()
        print(line+"\t耗时(s):"+str((endtime - starttime).seconds))

    except IOError:
        pass
    fileWrited.close()
    
def makeTodayDirStr():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = os.path.join("e:/webScrapy/",strToday,dirCurDownload)
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath

def parse_downloadFile(sound_ids):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    goalFilePath ="下载地址_"+dirCurDownload+"_"+".txt"
    fileWrited=open(goalFilePath, 'w')
    try:
        starttime = datetime.now()
        dirToday = makeTodayDirStr()
        for sound_id in sound_ids:

            urladdress = 'http://www.ximalaya.com/tracks/' + sound_id + '.json'  
            music_json = requests.get(urladdress,headers=headers).json()
            if 'title' in music_json.keys() and 'play_path_32' in music_json.keys():  
                line = music_json['title']+'\t'+music_json['play_path_32']
                print(line)
                fileWrited.write(line+"\n")
                saveFileName =os.path.join(dirToday,music_json['title'] + '.mp3')
                if not os.path.exists(saveFileName): 
                    try:
                        urllib.request.urlretrieve(music_json['play_path_32'], saveFileName )
                    except IOError:
                        continue
                

        endtime = datetime.now()
        print(line+"\t耗时(s):"+str((endtime - starttime).seconds))

    except IOError:
        pass
    fileWrited.close()



if __name__ == '__main__':

    
    sound_ids = []
    print(urladdress)
    sound_idsLine = get_ids(urladdress)
    if sound_idsLine != "":
        sound_ids.extend(sound_idsLine.split(','))
        
    print(sound_ids)
    parse_downloadFile(set(sound_ids))

    
