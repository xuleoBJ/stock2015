# -*- coding: cp936 -*-
import os
import shutil

INVALID_VALUE=-999
##从TXT格式测井曲线中提取所需要的系列。
if __name__=="__main__":


    sourceDirPath="log_txt"
    goalDirPath='log_txt_ex'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
    
    fileNames=os.listdir(sourceDirPath)
    
    seriersNames=['DEPTH','SP','GR','DEN','CNL','AC','LLD','LLS','RT90']

    for fileItem in fileNames:
        print ('-'*10,'Current deal...'+fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        fileWrited=open(goalDirPath+'\\'+fileItem,'w')
        lineIndex=0
        logIndexSelected_intList=[]
        for line in fileOpened.readlines():
            lineIndex+=1
            splitLine=line.upper().split()
            if lineIndex==1:
                print (line)
                fileWrited.write('\t'.join(seriersNames)+'\n')
                for item in seriersNames:
                    if item in splitLine:
                        logIndexSelected_intList.append(splitLine.index(item))
                    else:
                        print(fileItem+"缺失所需测井系列---"+item)
                        logIndexSelected_intList.append(INVALID_VALUE)
            if lineIndex>1:
                line=""
                for item in logIndexSelected_intList:
                    if item>=0:
                        line=line+splitLine[item]+'\t'
                    else:
                        line=line+str(INVALID_VALUE)+'\t'
                fileWrited.write(line+'\n')
        print(fileItem,logIndexSelected_intList)


    fileWrited.close()
