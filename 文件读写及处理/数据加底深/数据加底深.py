# -*- coding: cp936 -*-
import os
import shutil
##Ϊpetrel��һ�е�

columnIndex=0

if __name__=="__main__":

    sourceFile="fc_xl_20131022.txt"
    goalDirPath='FC_new.txt'

        
    fileOpened=open(sourceFile,'r')
    fileWrited=open(goalDirPath,'w')
    lineIndex=0
    lineList=[]
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            lineList.append(line)
    for i in range(0,len(lineList)-1):##��������1,����������0
        splitLine=lineList[i].split()
        splitNextLine=lineList[i+1].split()
        if len(splitLine)!=7:
            print i,line
        elif splitNextLine[0]==splitLine[0]:
            fileWrited.write('\t'.join(splitLine)+'\t'+splitNextLine[6]+'\n')
        else:
            fileWrited.write('\t'.join(splitLine)+'\t'+splitLine[1]+'\n')
   ##���һ�д���
    splitLine=lineList[-1].split()
    fileWrited.write('\t'.join(splitLine)+'\t'+splitLine[1]+'\n')
    


    fileWrited.close()




