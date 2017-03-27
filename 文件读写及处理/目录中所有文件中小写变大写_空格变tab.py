# -*- coding: cp936 -*-
import os
import shutil

def space2TabAnd2Upper(filePath_space,filePath_tab):
        fileOpened_space=open(filePath_space,'r')
        fileWrited_txtLog=open(filePath_tab,'w')
        lineIndex=0
        for line in fileOpened_space.readlines():
            lineIndex+=1
            splitLine=line.split()
            for i in range(len(splitLine)):
                splitLine[i]=splitLine[i].upper()
            fileWrited_txtLog.write('\t'.join(splitLine)+'\n')
        fileWrited_txtLog.close()
        print(filePath_space+"convert to tab complete.")

if __name__=="__main__":

    sourceDirPath="testData"
    goalDirPath='222'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
    
    ##  把操作目录下文件存入filenameslist
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        fileOpened=sourceDirPath+'\\'+fileItem
        fileWrited=goalDirPath+'\\'+fileItem
        space2TabAnd2Upper(fileOpened,fileWrited)


    print("新文件在"+goalDirPath)
