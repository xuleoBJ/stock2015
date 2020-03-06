# -*- coding: cp936 -*-
import os
import shutil

topDepthcolumnIndex=2
bottomDepthcolumnIndex=3

if __name__=="__main__":

    sourceFile="FC.txt"
    goalDirPath='errMessage.txt'

        
    fileOpened=open(sourceFile,'r')
    fileWrited=open(goalDirPath,'w')
    lineIndex=0
    lineList=[]
    strList=[]
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            lineList.append(line)
    for i in range(1,len(lineList)):##带标题行1,不带标题行0
        splitLine=lineList[i].split()
        splitLastLine=lineList[i-1].split()
        if splitLastLine[0]==splitLine[0]:
            if float(splitLine[topDepthcolumnIndex])!=float(splitLastLine[bottomDepthcolumnIndex]):
                print(str(i)+" depth err.")
                fileWrited.write(str(i)+" depth err.\n")
            if float(splitLine[topDepthcolumnIndex])<float(splitLastLine[topDepthcolumnIndex]):
                print(str(i)+" top and bottom err.")
                fileWrited.write(str(i)+" top and bottom err.\n")


    print("新文件在"+goalDirPath)
    fileWrited.close()




