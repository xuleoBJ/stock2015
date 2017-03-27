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
            line=line.replace('Ⅵ','VI')
            line=line.replace('Ⅶ','VII')
            line=line.replace('Ⅷ','VIII')
            line=line.replace('Ⅸ','IX')
            line=line.replace('Ⅹ','X')
            line=line.replace('Ⅺ','XI')
            line=line.replace('Ⅻ','XII')
            line=line.replace('Ⅰ','I')
            line=line.replace('Ⅱ','II')
            line=line.replace('Ⅲ','III')
            line=line.replace('Ⅳ','IV')
            line=line.replace('Ⅴ','V')

    
            
            fileWrited.write(line)
    fileWrited.close()
    fileOpened.close()
    print("新文件在"+goalDirPath)
