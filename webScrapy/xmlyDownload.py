#coding=utf-8
import os
import urllib
import sys
import json
sys.path.append("..")
import common
class Xmly():

    URL_PRIFIX = "http://www.ximalaya.com/tracks/"
    def getJsonUrl(self,url):
        result = url.split('/')
        return result[len(result)-1]+".json"
    def getVoiceUrl(self,html):
        # print html
        jsonStr = json.loads(html)
        return jsonStr["title"].encode('utf-8'),jsonStr["play_path"]

    def download(self,url,filepath):
        jsonUrl = self.URL_PRIFIX + self.getJsonUrl(url)
        html = common.getHtml(jsonUrl)
        voiceTitle,voiceUrl = self.getVoiceUrl(html)
        common.download(voiceUrl,filepath,voiceTitle+'.m4a')

if __name__ == '__main__':
    url = "http://www.ximalaya.com/13163945/sound/10499951"
    xmly = Xmly()
    xmly.download(url,"/Users/cheng/Documents/PyScript/res/")
