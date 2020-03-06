# -*- coding: cp936 -*-
import shutil
import os,sys

if __name__=="__main__":

    sourceDirPath="111"
    goalDirPath='替换名文件夹'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
    fileNames=os.listdir(sourceDirPath)

    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        fileWrited=open(goalDirPath+'\\'+fileItem,'w')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex+=1
            if line !="":
                splitLine=line.split()
                fileWrited.write('\t'.join(splitLine)+'\n')
    fileWrited.close()
    print("新文件在"+goalDirPath)
