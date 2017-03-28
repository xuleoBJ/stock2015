import sys
from PyQt4 import QtGui,QtCore
import urllib
import os
import re
import thread
import threading

class Main_QWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.website=QtGui.QLineEdit(self) #网址框
        self.filepath=QtGui.QLineEdit(self)  #路径框
        self.selectpathbutton=QtGui.QPushButton('select',self)
        self.tag=QtGui.QLabel('ready',self)  #状态
        downloadbutton=QtGui.QPushButton('download',self)

        grid=QtGui.QGridLayout()
        grid.addWidget(self.website,0,0,1,3)
        grid.addWidget(self.filepath,1,0,1,2)
        grid.addWidget(self.selectpathbutton,1,2)
        grid.addWidget(downloadbutton,2,0)
        grid.addWidget(self.tag,2,2)

        self.resize(300,300)
        self.setLayout(grid)
        self.setWindowTitle("download image")

        self.connect(self.selectpathbutton,QtCore.SIGNAL('clicked()'),self.selectPath)
        self.connect(downloadbutton,QtCore.SIGNAL('clicked()'),download)

    def getWebsite(self):
        return self.website.text() #获取网址的函数
    def getFilePath(self):  
        return self.filepath.text() #获取文件路径的函数
    def setTag(self,downloadtag):   
        self.tag.setText(downloadtag) #显示状态
    def selectPath(self):
        fileName = QtGui.QFileDialog.getExistingDirectory( self, 'Open' )
        self.filepath.setText(fileName)
        return fileName
    
class mythread(threading.Thread):
    def __init__(self,Website,FilePath):
        threading.Thread.__init__(self)
        self.Website=Website
        self.FilePath=FilePath
    def run(self):
        html=getHtml(self.Website)
        print self.Website
        print self.FilePath
        getImg(html,self.FilePath)
        main.setTag('finsh') #下载完毕后，将状态改为完成
        
def download():
    Website=unicode(main.getWebsite(),'utf-8').encode('utf-8')
    FilePath=main.getFilePath()
    main.setTag('go')
    #thread.start_new_thread(run,(Website,FilePath))
    t=mythread(Website,FilePath) #新建一个线程，传入参数
    t.start()  
   # while not t.isAlive():
    #    main.setTag('finish')
    #html=getHtml(Website)
    #print html
    #getImg(html,FilePath)
    #print path

    
def getHtml(url):
    return urllib.urlopen(url).read() #返回网页源码

def getImg(html,path):
    reg=re.compile(r'src="(.*?\.(jpg|gif|png))"')
    imglist=reg.findall(html)
    print len(imglist)
    x=0
    for imgurl in imglist:
        print imgurl
        main.setTag(str(x)+'/'+str(len(imglist))) #在状态栏上显示进度
        if imgurl[1]=='gif':
            xpath=path+'\%d.gif' % x
            urllib.urlretrieve(imgurl[0],xpath)
        elif imgurl[1]=='png':
            xpath=path+'\%d.png' % x
            urllib.urlretrieve(imgurl[0],xpath)
        else:
            xpath=path+'\%d.jpg' % x
            urllib.urlretrieve(imgurl[0],xpath)
        x+=1
    print 'finish--------'

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    main=Main_QWidget()
    main.show()
    sys.exit(app.exec_())

