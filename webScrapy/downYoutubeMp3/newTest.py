import webbrowser
import urllib.request
import os
import sys
from datetime import datetime

def reporthook(count,block_size,total_size):
	"""
	回调函数
	下载进度现实的函数
	@count 已经下载的数据块的个数 是个数哦
	@block_size 数据会的大小，一般都是多少多少字节哦
	@totol_size 总的文件大小
	
	有了这三个量我们就可以计算进度了哈
	只要totol_size 等于 count * block_size 那就说明下载完毕了

	""" 
	percent = (100.0 * count * block_size ) / total_size
	#per就是百分进度了
	sys.stdout.write("%2d%%" % percent)
	sys.stdout.write("\b\b\b")
	sys.stdout.flush()
	#sys.stdout.write("Download Percent: %.2f %%"% per)
	#输出进度,保留两个百分点，stdout。write("\r")是每次输出光标回到行首，这样目的为了一行输出进度，print xxx, 逗号在print后面表示不换行
    
def makeTodayDirStr():
    strToday = datetime.now().strftime("%Y%m%d")
    strPath = "e:/webScrapy/"+strToday
    if not os.path.exists(strPath):
        os.makedirs(strPath)
    return strPath

if __name__=="__main__":
    sourceFile="downloadAddress.txt"
    fileOpened=open(sourceFile,'r')
    url_strList=[]
    lineIndex=0
    for line in fileOpened.readlines():
        lineInex = lineIndex +1
        print (line)
        if lineIndex >= 0 :
            url_strList.append(line)
   # print (url_strList )
    dirToday = makeTodayDirStr()
    for url in url_strList:
        # Open URL in new window, raising the window if possible.
        
        localName = os.path.basename(url)
        fileNameChinese = urllib.parse.unquote(localName)
        local =dirToday+"\\"+urllib.parse.unquote(fileNameChinese)
        print ("-"*20+"正在下载：  "+fileNameChinese)
        aa=urllib.request.urlopen(url)
        print (fileNameChinese + " OK")
        
