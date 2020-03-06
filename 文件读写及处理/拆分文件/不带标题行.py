# -*- coding: cp936 -*-
import os
import shutil
##按某一列分解文件,第一行为文件头

columnIndex=2

if __name__=="__main__":

    sourceFile="111.txt"
    goalDirPath='分解文件'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
        
    fileOpened=open(sourceFile,'r')
    lineIndex=0
    fileName_strList=[]
    fileNameWrited="头一行"
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
    print("新文件在"+goalDirPath)




