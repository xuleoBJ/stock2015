# -*- coding: cp936 -*-
import os
import shutil

columnIndex=2  ##请输入列数 从0开始
SetTitleLine=0  ##带文件头取1，不带文件头取0
FirstDataLine=0  ##数据起始行

if __name__=="__main__":

    sourceFile="f41.txt"  ##原文件名
    goalDirPath='t41_fault'     ##保存文件夹
    
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
        
    fileOpened=open(sourceFile,'r')
    lineIndex=0
    lineList=[]
    titleLine=""
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            lineList.append(line)
    
    for i in range(FirstDataLine,len(lineList)):
        splitLine=lineList[i].split()
        splitLastLine=lineList[i-1].split()
        if splitLastLine[columnIndex]!=splitLine[columnIndex]:
           fileNameWrited=splitLine[columnIndex]
           fileWrited=open(goalDirPath+'\\'+fileNameWrited+'.txt','w')
           if SetTitleLine==1:
               fileWrited.write(lineList[0]+lineList[i])
           else:
               fileWrited.write(lineList[i])
        else:
           fileWrited.write(lineList[i])
    

    fileWrited.close()
    print("新文件在"+goalDirPath)




