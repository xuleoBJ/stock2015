import datetime
import lxml.etree as etree
import lxml.html
import ConfigParser
import time,sched,os,urllib2,re,string
import ctypes

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

def event_func():
    goalFilePath=os.path.join(resultDir,'news.txt')
    fileWrited=open(goalFilePath,'w')
    num=0
    urlLink="http://www.news.cn/fortune/"
    lineList=[]
    try:
        currentTimeStr= time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
        print currentTimeStr
        print "start:"+urlLink
        req=urllib2.Request(urlLink)
        response=urllib2.urlopen(req)
        if response.code==200:
            html=response.read()
            parsed_html = lxml.html.fromstring(html)
    ##        print type(parsed_html)
            for elem in parsed_html.xpath("//div[@class='headNews']/h2"):
                newOne=elem.text_content()
                if not newOne in newsList:
                    newsList.append(elem.text_content())
                    print num,newOne
                    now = datetime.datetime.now()
                    startTime = now.replace(hour=9, minute=30, second=0, microsecond=0)
                    endTime= now.replace(hour=15, minute=0, second=0, microsecond=0)
                    if startTime<=now<=endTime:
                        ctypes.windll.user32.MessageBoxA(0,"new news!!", currentTimeStr, 1)
                num=num+1
            for elem in parsed_html.xpath("//p[@class='ywzy']/a"):
                newOne=elem.text_content()
                if not newOne in newsList:
                    newsList.append(elem.text_content())
                    print num,newOne
                    now = datetime.datetime.now()
                    startTime = now.replace(hour=9, minute=30, second=0, microsecond=0)
                    endTime= now.replace(hour=15, minute=0, second=0, microsecond=0)
                    if startTime<=now<=endTime:
                        ctypes.windll.user32.MessageBoxA(0,"new news!!", currentTimeStr, 1)
                num=num+1
               ## fileWrited.write(elem.text_content())
    except urllib2.HTTPError,e:
        print "server error"
        print e.code
    except urllib2.URLError,e:
        print "URLError:"
        print e.reason
 ##   for line in lineList:
 ##       print line
 ##       fileWrited.write(line)
    fileWrited.close()

def perform(inc):
    s.enter(inc,0,perform,(inc,))
    event_func()

def mymain(inc=90):
    if not os.path.exists(resultDir):
        os.makedirs(resultDir)
    s.enter(0,0,perform,(inc,))
    s.run()

if __name__ == "__main__":
    mymain()



