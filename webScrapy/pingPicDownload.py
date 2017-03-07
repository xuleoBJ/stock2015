import urllib.request
import re
import time

def getHtml(url):
    return  urllib.request.urlopen(url).read()

def getImgUrl(html):
    reg=re.compile(r'(http://s.cn.bing.net/.*?\.jpg)') #正则式
    url=reg.findall(html)
    print (url[0])
    return url[0]

def downloadImg(url,path):
    xpath=path+'\\bing.jpg'
    print (xpath)
    urllib.urlretrieve(url,xpath)

def makeDownLoadDir():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = "e:/webScrapy/"+strToday

    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath
    
if __name__=='__main__':
    start=time.time()
    html=getHtml('http://cn.bing.com/')
    url=getImgUrl(html)
    downloadImg(url,strPath)
    end=time.time()
    print ('done %.2f seconds' % (end-start))
