# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    sourceDirPath="testData"
    goalDirPath='替换字符后文件夹'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
        
    fileNames=os.listdir(sourceDirPath)

    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        fileWrited=open(goalDirPath+'\\'+fileItem.lower(),'w')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex+=1
            line=line.replace('油井','3')
            line=line.replace('水井','15')
            line=line.replace('东','d')
            line=line.replace('试','shi')
            line=line.replace('砂','sha')
            line=line.replace('英','y')

            fileWrited.write(line)
    fileWrited.close()
    print("新文件在"+goalDirPath)
