# -*- coding:utf-8 -*- 

import urllib.request
import json
import os
import sys
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime 


##dirCurDownload是标签，urladdress是单页地址
## parse_downloadText 只把下载地址保存到文本
## parse_downloadFile 下载文件到目录

dirCurDownload ="老友记 六人行 Friends 第二季"
urladdress ="http://www.ximalaya.com/14528172/album/387636"


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
                saveFileName =os.path.join(dirToday,music_json['title'] + '.m4a')
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

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    print(BASE_DIR)
    sound_ids = []
    print(urladdress)
    if sound_idsLine != "":
        sound_ids.extend(sound_idsLine.split(','))
        
    print(sound_ids)
    parse_downloadFile(set(sound_ids))

    
