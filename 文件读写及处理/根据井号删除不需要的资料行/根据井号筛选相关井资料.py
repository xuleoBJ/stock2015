# -*- coding: cp936 -*-
import os

if __name__=="__main__":

##    print("当前工作路径：",os.getcwd())


    wellName=os.path.basename(os.getcwd())
    print ('根据井号筛选井资料，删除不需要的资料行：')
    
    fileName_jh="jh.txt"
    fileName_Original="jscgb.txt"
    
    openFileWrite="newFile.txt"



    fileOpened_Original=open(fileName_Original,'r')
    fileOpened_jh=open(fileName_jh,'r')
    fileWrited=open(openFileWrite,'w')



    welllName_list=[]
    for lineWellName in fileOpened_jh.readlines():
        if lineWellName!="":
            splitlineWellName=lineWellName.split()
            welllName_list.append(splitlineWellName[0])

            
    lineIndex=0
    for line in fileOpened_Original.readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>=1:
            splitline=line.split()
            jh=splitline[0]
            if jh in welllName_list:
                fileWrited.write(line)
                
    
    fileWrited.close()
    
