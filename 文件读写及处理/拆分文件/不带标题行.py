# -*- coding: cp936 -*-
import os
import shutil
##��ĳһ�зֽ��ļ�,��һ��Ϊ�ļ�ͷ

columnIndex=2

if __name__=="__main__":

    sourceFile="111.txt"
    goalDirPath='�ֽ��ļ�'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
        
    fileOpened=open(sourceFile,'r')
    lineIndex=0
    fileName_strList=[]
    fileNameWrited="ͷһ��"
    for line in fileOpened.readlines():
        lineIndex+=1
        if line!="" and lineIndex>1:
            splitLine=line.split()
            fileName_strList.append(splitLine[columnIndex])
            if fileNameWrited!=fileName_strList[-1]:
                fileNameWrited=splitLine[columnIndex]
                fileWrited=open(goalDirPath+'\\'+fileNameWrited+'.txt','w')
                fileWrited.write(line)
            else:
                fileWrited.write(line)
    fileWrited.close()
    print("���ļ���"+goalDirPath)




