from html.parser import HTMLParser
import urllib.request
import json
import os
import sys
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime 

## sID 是 用户ID
## dirCurDownload 保存目录

sID="12495477"
dirCurDownload ="吴晓波频道"
formatM4a="play_path_64"

def get_ids(urladdress):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
   
    r = requests.get(urladdress,headers=headers)

    if r.status_code == 200:
        dataJson = r.json()
        stringHtml = dataJson["html"]
        soup = BeautifulSoup(stringHtml, 'lxml')
        inforList = soup.find_all("ul")
        idsList =[]
        for item in inforList:
            if item.has_attr("sound_ids"):
                sound_idsLine = item["sound_ids"]
                return (sound_idsLine)
    else:
        return ""
    
def makeTodayDirStr():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = os.path.join("e:/webScrapy/",strToday,dirCurDownload)
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath

def parse_python_events(sound_ids):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    goalFilePath = sID+".txt"
    fileWrited=open(goalFilePath, 'w')
    try:
        starttime = datetime.now()
        endtime = datetime.now()
        dirToday = makeTodayDirStr()
        for sound_id in sound_ids:
            starttime = datetime.now()     
            urladdress = 'http://www.ximalaya.com/tracks/' + sound_id + '.json'  
            music_json = requests.get(urladdress,headers=headers).json()
            line =""
            if 'title' in music_json.keys() and formatM4a in music_json.keys():
                if music_json['title'] != None and music_json[formatM4a] !=None:
                    line = 'downloading:\t'+music_json['title']+'\t'+music_json[formatM4a]
                    print(line)
                    fileWrited.write(line+"\n")
                    saveFileName =os.path.join(dirToday,music_json['title'] + '.m4a')
                    if not os.path.exists(saveFileName): 
                        try:
                            urllib.request.urlretrieve(music_json[formatM4a], saveFileName )
                        except IOError:
                            continue
            endtime = datetime.now()
            print(line+"\t耗时(s):"+str((endtime - starttime).seconds))
    except IOError:
        pass
    fileWrited.close()

if __name__ == '__main__':
   
    sound_ids = []
    for i in range(1,34):
        urladdress ='http://www.ximalaya.com/%s/index_tracks?page=%d'%(sID,i)
        print(urladdress)
        sound_idsLine = get_ids(urladdress)
        if sound_idsLine != "":
            sound_ids.extend(sound_idsLine.split(','))
    print(sound_ids)
    parse_python_events(set(sound_ids))

    
