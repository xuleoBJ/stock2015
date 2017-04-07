#!coding:utf-8
#!coding:/usr/bin/python 
"""
dependency:
	you have to install  beautifulsoup4 modulex
	sudo pip install beautifulsoup4

description:
 ximalaya downloading program made by Meyou(Wuhan) --2015.4.27
 feel free to use it 

usage:
 1:just one page to download
 		python xmly.py  album_url 
 2:many pages  to download
 		python xmly.py album_url start_page_number  end_page_number


notice:
 after finishing downloading the album ,please remove the temporary json file.
"""
import sys
import os
import urllib.request
from bs4 import BeautifulSoup
import re


def get_ids(curHtlm):
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
	
            idsList.extend(sound_idsLine.split(','))
        else:
            pass
        # child_herf = item.find("a")
        # printLine = child_herf.attrs["title"]+"\t"+child_herf.attrs["href"]
        # print(printLine) 
        # fileWrited.write(printLine+"\n")
    print(set(idsList))
    fileWrited.close()

def dlone(id):
	#http://www.ximalaya.com/tracks/5500449.json
	#print "in dlone "
	base="http://www.ximalaya.com/tracks/"
	url=base+str(id)+".json"
	#print url
	#fd=urllib2.urlopen(url)
	filename="./json/"+str(id)+".json"
	if not os.path.isfile(filename): 
		#cmd="wget "+url
		#os.system(cmd)
		dljson({"filename":filename,"url":url})
	fd=open(filename)
	json_paser(fd.read())

def json_paser(content):
	#print "in sjon_paser"
	import json
	myjson=json.loads(content)
	#print myjson["title"]
	#print myjson["play_path_64"]
	title= myjson["title"]+".mp3"
	mp3=myjson["play_path_64"]
## 	if "mp3" not in mp3:
##                        print ("url is werid:",mp3)
	#http://101.4.136.34:9999/fdfs.xmcdn.com/group6/M05/36/CF/wKgDg1TgOM3QGSfLATJ1WHmo2b0255.mp3
	base="http://101.4.136.34:9999/fdfs.xmcdn.com/"
	url=base+mp3
	#print url 
	import os 
	#cmd="wget "+ url+ " -O "+title+".mp3"
	#os.system(cmd)

	dlonemp3({"filename":title,"url":url})

def dllist(idlist):
	if not os.path.isdir("./json"):
		os.mkdir("json")

	for id in idlist:
		dlone(id)
def dlonemp3(mp3dict):                 #下载mp3音频文件
	filename=mp3dict["filename"]
	url=mp3dict["url"]
	if not os.path.isfile(filename):     #如果没有下载过
		print ("downloading",filename)
		dlafile(filename,url)
	else:
		print ("already downloaded this file:"+filename)
def dljson(jsondict):                 #下载mp3音频文件
	filename=jsondict["filename"]
	url=jsondict["url"]
	if not os.path.isfile(filename):     #如果没有下载过
		print ("downloading",filename)
		dlafile(filename,url,1024)
	else:
		print ("already downloaded this file:"+filename)

def dlafile(filename,url,size=1024*1024*10):
        """
        通用程序，给出文件名和url后，下载文件
        """
        #print url
        CHUNK=size
        #print url
        req=urlopen(url)
        size=int(req.info()["Content-Length"])
        ALL=size/CHUNK+1
        now=0
        #print "下载中 "+filename+"["+str(size/1000)+"KiB]"
        with open(filename,"wb") as fp:
            while True:
                condition=int(float(now)*100/ALL)
                if condition >100:
                    condition=100
                print ("\033[91m\r[%"+str(condition)+"]\033[0m",)
                sys.stdout.flush()
                chunk=req.read(CHUNK)
                if not chunk: break
                fp.write(chunk)
                now+=1

        print ("\n")	
def downLoadAllAudio(url):
	idlist=get_ids(url)
	dllist(idlist)
def dlpages(urlfirst,start,end):
	"""
	 function:download many pages at one time
	 usage: python xmly.py  album_url  startnumber  endnumber
	"""
	for i in range(start,end+1):
		realurl=urlfirst+"?page="+str(i)
		print ("page ",i,"is downloading...")
		dlall(str(realurl))

if __name__=="__main__":
    album_addrs = []
    album_folder = ""
    filePath = 'E:\\stock2015\\webScrapy\\FM下载\\albumaddr.txt'
    #本地文件存储专辑链接地址，可以一次下载多个专辑
    with open(filePath,'r') as addr_file:
        album_addrs = addr_file.readlines()
    print(album_addrs)

	


