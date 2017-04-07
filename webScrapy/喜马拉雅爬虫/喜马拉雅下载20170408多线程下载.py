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
sID="43087355"

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
    strPath = "e:/webScrapy/"+strToday
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath



def parse_python_events(sound_ids):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    goalFilePath = sID+".txt"
    dirToday = makeTodayDirStr()
    fileWrited=open(goalFilePath, 'w')
    try:
        starttime = datetime.now()
        endtime = datetime.now()
        for sound_id in sound_ids:
            starttime = datetime.now()
            urladdress = 'http://www.ximalaya.com/tracks/' + sound_id + '.json'  
            music_json = requests.get(urladdress,headers=headers).json()
            if 'title' in music_json.keys() and 'play_path_32' in music_json.keys():
                print('downloading:')
                line = music_json['title']+'\t'+music_json['play_path_32']
                fileWrited.write(line+"\n")
                saveFileName =os.path.join(dirToday,music_json['title'] + '.mp3')
                if not os.path.exists(saveFileName): 
                    try:
                        down = downloader(music_json['play_path_32'], saveFileName)
                        down.run()
                        #urllib.request.urlretrieve(music_json['play_path_32'], saveFileName )
                    except IOError:
                        continue
            endtime = datetime.now()
            print(line+"\t耗时(s):"+str((endtime - starttime).seconds))

    except IOError:
        pass
    fileWrited.close()

class downloader:
    # 构造函数
    def __init__(self,strUrl,SavefilePath):
        # 要下载的数据连接
        self.url=strUrl
        # 要开的线程数
        self.num=8
        # 存储文件的名字，从url最后面取
        self.name=SavefilePath
        # head方法去请求url
        r = requests.head(self.url)
        # headers中取出数据的长度
        self.total = int(r.headers['Content-Length'])
        #print type('total is %s' % (self.total))
    def get_range(self):
        ranges=[]
        # 比如total是50,线程数是4个。offset就是12
        offset = int(self.total/self.num)
        for i in  range(self.num):
            if i==self.num-1:
                # 最后一个线程，不指定结束位置，取到最后
                ranges.append((i*offset,''))
            else:
                # 每个线程取得区间
                ranges.append((i*offset,(i+1)*offset))
        # range大概是[(0,12),(12,24),(25,36),(36,'')]
        return ranges
    def run(self):

        f = open(self.name,'wb')
        for ran in self.get_range():
            # 拼出Range参数 获取分片数据
            r = requests.get(self.url,headers={'Range':'Bytes=%s-%s' % ran,'Accept-Encoding':'*'})
            # seek到相应位置
            f.seek(ran[0])
            # 写数据
            f.write(r.content)
        f.close()

if __name__ == '__main__':

    
    sound_ids = []
    for i in range(1,3):
        urladdress ='http://www.ximalaya.com/%s/index_tracks?page=%d'%(sID,i)
        print(urladdress)
        sound_idsLine = get_ids(urladdress)
        if sound_idsLine != "":
            sound_ids.extend(sound_idsLine.split(','))
    print(sound_ids)
    parse_python_events(set(sound_ids))

    
