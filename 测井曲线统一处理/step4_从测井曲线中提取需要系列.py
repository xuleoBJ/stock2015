# -*- coding: cp936 -*-
import os
import shutil

i_INVALID_VALUE=-999
##从TXT格式测井曲线中提取所需要的系列。
if __name__=="__main__":


    dirPathLogFileTxt="log_txt"
    dirPathGoal='log_txt_ex'
    if os.path.exists(dirPathGoal):
        shutil.rmtree(dirPathGoal)
    os.mkdir(dirPathGoal)
        
    seriersNames=['DEPT.M','PORT.','PERM.','SO.']

    for fileItem in os.listdir(dirPathLogFileTxt):
        print ('-'*10,'Current deal...'+fileItem)
        fileOpened=open(dirPathLogFileTxt+'\\'+fileItem,'r')
        fileWrited=open(dirPathGoal+'\\'+fileItem,'w')
        lineIndex=0
        indexListSelectedLog=[]
        for line in fileOpened.readlines():
            lineIndex+=1
            splitLine=line.upper().split()
            if lineIndex==1:
                fileWrited.write('\t'.join(seriersNames)+'\n')
                for item in seriersNames:
                    if item in splitLine:
                        indexListSelectedLog.append(splitLine.index(item))
                    else:
                        print(fileItem+"缺失所需测井系列---"+item)
                        indexListSelectedLog.append(i_INVALID_VALUE)
            if lineIndex>1:
                sListWrited=[]
##                print(indexListSelectedLog)
                for indexItemLog in indexListSelectedLog:
                    if indexItemLog>=0:
                        sListWrited.append(splitLine[indexItemLog])
                    else:
                        sListWrited.append(str(i_INVALID_VALUE))
                fileWrited.write('\t'.join(sListWrited)+'\n')
        fileOpened.close()
        print(fileItem,indexListSelectedLog)


    fileWrited.close()
