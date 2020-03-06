# -*- coding: cp936 -*-
import os
import shutil

def forward2txt(filePath_forwardLog,filePath_txtLog):
        fileOpened_forwardLog=open(filePath_forwardLog,'r')
        fileWrited_txtLog=open(filePath_txtLog,'w')
        lineIndex=0
        flag=False
        for line in fileOpened_forwardLog.readlines():
            lineIndex+=1
            if line.startswith('#'):
                flag=True
                line=line.replace('#','').upper() #转大写
                splitLine=line.split()
                temp='\t'.join(splitLine)
                fileWrited_txtLog.write(temp+'\n')

            elif flag==True and line.strip()!='':
                splitLine=line.split()
                temp='\t'.join(splitLine)
                fileWrited_txtLog.write(temp+'\n')
        fileWrited_txtLog.close()
        print(filePath_forwardLog+"convert to txtlog complete.")
    
    

if __name__=="__main__":
    
    sourceDirPath="ydLog"
    goalDirPath='log_txt'
    
    print ('prepare forward2txt to ',goalDirPath)
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)

    ##  把操作目录下文件存入filenameslist
    fileNames=os.listdir(sourceDirPath)
    for wellItem in fileNames:
        print ('forward2txt...'+'-'*10,wellItem)
        fileOpened=sourceDirPath+'\\'+wellItem
        fileWrited=goalDirPath+'\\'+wellItem
        forward2txt(fileOpened,fileWrited)
        

    print("处理完毕")
