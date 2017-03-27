# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据井号筛选井资料，删除不需要的资料行：')
    
    fileName_jh="jh_notINb.txt"
    fileOpened_jh=open(fileName_jh,'r')
    sList_jh=[]
    for lineWellName in fileOpened_jh.readlines():
        if lineWellName!="":
            splitlineWellName=lineWellName.split(',')
            sList_jh.extend(splitlineWellName)
    fileOpened_jh.close()

    print(sList_jh)
            
    lineIndex=0
    filePathList=[]
    filePathList.append("$UserData#//$wellHead#.txt")
    filePathList.append("$UserData#//$layerDepth#.txt")
    filePathList.append("$UserData#//$interpretation#.txt")
    for itemFilePath in filePathList:
         fileOpened_OriginalFile=open(itemFilePath,'r')
         openFileWrited=itemFilePath.replace(".txt",fileName_jh);
         fileWrited=open(openFileWrited,'w')
         for line in fileOpened_OriginalFile.readlines():
            lineIndex=lineIndex+1
            if line!="" and lineIndex>=1:
                splitline=line.split()
                jh=splitline[0]
 
                if not (jh in sList_jh):
                    fileWrited.write(line)
         fileOpened_OriginalFile.close()
         fileWrited.close()
         print (itemFilePath+'OK.')
    
