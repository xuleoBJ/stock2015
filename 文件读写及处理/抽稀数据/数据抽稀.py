# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    sourceDirPath="original"
    goalDirPath='changed'
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
            if lineIndex>1 and lineIndex%20==1:
                fileWrited.write(line)
            
    
            
            
    fileWrited.close()
    fileOpened.close()
    print("新文件在"+goalDirPath)
