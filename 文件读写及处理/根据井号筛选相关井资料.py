# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据井号筛选井资料，删除不需要的资料行：')
    
    fileName_jh="changed\\jh_need.txt"
    fileOpened_jh=open(fileName_jh,'r')
    sList_jh=[]
    for lineWellName in fileOpened_jh.readlines():
        if lineWellName!="":
            splitlineWellName=lineWellName.split()
            sList_jh.append(splitlineWellName[0])
    fileOpened_jh.close()

    
    fileName_firstHand="changed\\wellhead20131018.txt"

    openFileWrite="_result.txt"


    fileOpened_firstHand=open(fileName_firstHand,'r')
    
    fileWrited=open(openFileWrite,'w')


            
    lineIndex=0
    for line in fileOpened_firstHand.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            splitline=line.split()
            jh=splitline[0]
            if jh in sList_jh:
                fileWrited.write(line)
    fileOpened_firstHand.close()         
    
    fileWrited.close()
    print ('OK.')
    
