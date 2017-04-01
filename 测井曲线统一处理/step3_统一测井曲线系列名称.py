# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    sourceDirPath="log_txt"
    goalDirPath='changedChar'
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
            line=line.replace('AC%3','AC')
            line=line.replace('AC%2','AC')
            line=line.replace('GRRD%3','GR')
            line=line.replace('GRRD%2','GR')
            line=line.replace('AC%1','AC')
            line=line.replace('%4','')
            line=line.replace('%3','')
            line=line.replace('%2','')
            line=line.replace('%1','')
            fileWrited.write(line)
    fileWrited.close()
    print("新文件在"+goalDirPath)

