# -*- coding: cp936 -*-
import os
import shutil
##为petrel加一行底

columnIndex=0

if __name__=="__main__":

    sourceFile="B6.txt"
    goalDirPath='B6_new.txt'

        
    fileOpened=open(sourceFile,'r')
    fileWrited=open(goalDirPath,'w')
    lineIndex=0
    lineList=[]
    jhList=[]
    yxhd=[]
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.strip().split()
        if line!="" and lineIndex>1:
            lineList.append(line)
            jhList.append(splitLine[0])
            yxhd.append(float(splitLine[5]))
    for item in set(jhList):
        sumYXHD=[]
        for i in range(len(jhList)):
            if jhList[i]==item:
                sumYXHD.append(yxhd[i])
        avg=sum(sumYXHD)/len(sumYXHD)
        fileWrited.write(item+'\t'+str(sum(sumYXHD))+'\n')

    fileWrited.close()
    print("OK")



