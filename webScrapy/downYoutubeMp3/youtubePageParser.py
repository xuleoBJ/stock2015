import urllib.request
from bs4 import BeautifulSoup

goalFilePath='youtube_addr.txt'
fileWrited=open(goalFilePath,'w')
#curHtlm = urllib.request.urlopen('https://www.zhihu.com/')
curHtlm = "D://downLoadWebpage//大唐雷音寺｜全集｜持续更新中... - YouTube.html"
soup = BeautifulSoup(open(curHtlm,encoding = "utf-8").read(),'lxml')
#print(soup.prettify())
print (soup.title)
inforList = soup.find_all('div',{'class':'content-wrapper'})
for item in inforList:
    child_herf = item.find("a")
    printLine = child_herf.attrs["title"]+"\t"+child_herf.attrs["href"]
    print(printLine) 
    fileWrited.write(printLine+"\n")
fileWrited.close()


