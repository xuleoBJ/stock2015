# -*- coding: cp936 -*-
import os
import shutil
##Ϊpetrel��һ�е�

columnIndex=0

if __name__=="__main__":

    sourceFile="FC.txt"
    goalDirPath='FC_2.txt'

        
    fileOpened=open(sourceFile,'r')
    fileWrited=open(goalDirPath,'w')
    lineIndex=0
    lineList=[]
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            lineList.append(line)
    for i in range(1,len(lineList)):##��������1,����������0
        splitLine=lineList[i].split()
        splitLastLine=lineList[i-1].split()
        if splitLastLine[0]!=splitLine[0]:
            splitLastLine[1]="K"
            splitLastLine[2]=splitLastLine[3]
            lastLine='\t'.join(splitLastLine)
            fileWrited.write(lastLine+'\n')
            fileWrited.write(lineList[i])
        else:
            fileWrited.write(lineList[i])
            


   
    print("���ļ���"+goalDirPath)
    fileWrited.close()




