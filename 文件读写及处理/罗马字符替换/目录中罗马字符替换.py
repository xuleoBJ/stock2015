# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    sourceDirPath="$UserData#"
    goalDirPath='$UserData#changed'
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
            line=line.replace('��','I')
            line=line.replace('��','II')
            line=line.replace('��','III')
            line=line.replace('��','IV')
            line=line.replace('��','V')
            line=line.replace('��','VI')
            line=line.replace('��','VII')
            line=line.replace('��','VIII')
            line=line.replace('��','IX')
            line=line.replace('��','X')
            line=line.replace('��','XI')
            line=line.replace('��','XII')


    
            
            fileWrited.write(line)
    fileWrited.close()
    fileOpened.close()
    print(goalDirPath)
