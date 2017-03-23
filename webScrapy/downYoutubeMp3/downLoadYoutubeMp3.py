import webbrowser
import urllib.request
import os

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print ("%.2f%%")% percent

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
    print ( url_strList )   
    for url in url_strList:
        # Open URL in new window, raising the window if possible.
        print (url)
        localName = os.path.basename(url)
        local = 'd:\\'+localName
        urllib.request.urlretrieve(url, local)
        print (localName + " OK")
        
    #webbrowser.open_new(url)
    # Open URL in a new tab, if a browser window is already open.
    # webbrowser.open_new_tab(url)
