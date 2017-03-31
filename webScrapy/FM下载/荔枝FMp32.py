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
import sys ,os
import urllib.request
from bs4 import BeautifulSoup
import re


def get_lizhiMp3(filename,iPage=1):
        print(filename)
        html = urllib.request.urlopen(filename).read()#
##        content = html
##        pattern = re.compile('data-url')
##        match = pattern.match(content)
##        print (match)
        soup=BeautifulSoup(html,"lxml")
        print(soup.title)
        goalFilePath=str(iPage)+'_addr.txt'
        fileWrited=open(goalFilePath,'w')
        newlist=soup.find_all("a",{"class":"clearfix js-play-data audio-list-item"})
        for item in newlist:
#                print(item["data-title"])
                print(item["data-url"])
                fileWrited.write(item["data-url"]+"\t"+item["data-title"]+"\n")
        fileWrited.close()



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
        iMode = 2 #1为单个网页 其它为多页
        if iMode==1:
                strUrl="http://www.lizhi.fm/1359641/"
                get_lizhiMp3(strUrl)
        if iMode >1:
                for i in range(1,30):
                        strUrl="http://www.lizhi.fm/1481275/p/"+str(i)+".html"
                        get_lizhiMp3(strUrl,i)

	


