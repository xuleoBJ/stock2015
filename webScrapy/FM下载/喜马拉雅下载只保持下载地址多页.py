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
sID="1624974"
sName ="听电影学英语"

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

def parse_python_events(sound_ids):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    goalFilePath ="下载地址_"+sName+"_"+sID+".txt"
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

    
