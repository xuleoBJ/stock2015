# -*- coding: UTF-8 -*-
import datetime
import lxml.etree as etree
import lxml.html
import ConfigParser
import time,sched,os,urllib2,re,string
import ctypes
import pandas as pd
from bs4 import BeautifulSoup

resultDir="resultDir"
s = sched.scheduler(time.time,time.sleep)
newsList=[]
def writeConfig(websites):
    cf=ConfigParser.ConfigParser()
    configFilePath="config.ini"
    #cf.read(configFilePath)
    if os.path.isfile(configFilePath):
            os.remove(configFilePath)
    cf.add_section('webDir')  
    cf.set('webDir','websites',websites)
    ##jjcf.set('proxy','port','80')
    cf.write(open(configFilePath,"w")) 
'''
set proxy here
'''
enable_proxy = 1  
proxy_handler = urllib2.ProxyHandler({"http" : '10.22.96.29:8080'})  
null_proxy_handler = urllib2.ProxyHandler({})  
if enable_proxy:  
	opener = urllib2.build_opener(proxy_handler)  
else:  
	opener = urllib2.build_opener(null_proxy_handler)  
urllib2.install_opener(opener)  
##html_page = urllib2.urlopen(url)
##file_savelink=open("fileSave.txt","w")
print "starting:"

storeDir=datetime.date.today().strftime("%Y%m%d")

def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

def event_func_globleMarket():
    urlLink="http://quote.eastmoney.com/center/global.html#global_3"
    lineList=[]
    try:
        currentTimeStr= time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
        print currentTimeStr
        print "global market start:"+urlLink
        req=urllib2.Request(urlLink)
        response=urllib2.urlopen(req)
        if response.code==200:
            html=response.read()
            soup= BeautifulSoup(html,from_encoding="gb18030")
            table = soup.find("table", attrs={"id":"Asia"})
#            print(table.encode('gb18030'))
            
            NKY7 = table.find('tr',attrs={"id":"NKY7"}) 
            for tr in NKY7.findAll('td'):  
                print tr.text.encode("gb18030")  
    
  
#            parsed_html = lxml.html.fromstring(html)
#            ##修改xpath，得到相关新闻对应的xpath语法
#            for table in parsed_html.xpath("//table[@id='Asia']"):
#                header = [text(th) for th in table.xpath('//th')]        # 1
#                data = [[text(td) for td in tr.xpath('td')]  for tr in table.xpath('//tr')]                   # 2
#                data = [row for row in data if len(row)==len(header)]    # 3
#                data = pd.DataFrame(data, columns=header)                # 4
#                print(data)
#                newOne=elem.text_content()
#                print newOne
#                if not newOne in newsList:
#                    newsList.append(elem.text_content())
#                    now = datetime.datetime.now()
#                    startTime = now.replace(hour=8, minute=30, second=0, microsecond=0)
#                    endTime= now.replace(hour=17, minute=0, second=0, microsecond=0)
#                    if startTime<=now<=endTime:
#                        ctypes.windll.user32.MessageBoxA(0,"gwy_new news!!", currentTimeStr, 1)
    except urllib2.HTTPError,e:
        print "server error"
        print e.code
    except urllib2.URLError,e:
        print "URLError:"
        print e.reason


def perform(inc):
    s.enter(inc,0,perform,(inc,))
    event_func_globleMarket()

def mymain(inc=900):
    if not os.path.exists(resultDir):
        os.makedirs(resultDir)
    s.enter(0,0,perform,(inc,))
    s.run()

if __name__ == "__main__":
    mymain()



