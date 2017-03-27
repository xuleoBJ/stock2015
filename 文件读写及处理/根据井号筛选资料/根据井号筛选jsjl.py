# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据井号筛选井资料，删除不需要的资料行：')
    
    fileName_jh="B-K211201311JHperforated.txt"
    fileOpened_jh=open(fileName_jh,'r')
    sList_jh=[]
    for lineWellName in fileOpened_jh.readlines():
        if lineWellName!="":
            splitlineWellName=lineWellName.split()
            sList_jh.extend(splitlineWellName)
    fileOpened_jh.close()

    print(sList_jh)

    
    fileName_firstHand="$UserData#//$interpretation#.txt"


    openFileWrited=fileName_firstHand.replace(".txt",fileName_jh);
    fileWrited=open(openFileWrited,'w')


            
    lineIndex=0
    sListJH_firstHand=[]
    fileOpened_firstHand=open(fileName_firstHand,'r')
    for line in fileOpened_firstHand.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            splitline=line.split()
            jh=splitline[0]
            sListJH_firstHand.append(jh)
            if jh in sList_jh:
                fileWrited.write(line)
    fileOpened_firstHand.close()
    for item in sList_jh:
        if item not in set(sListJH_firstHand):
            print(item+" not find")
    
    fileWrited.close()
    print ('OK.')
    
