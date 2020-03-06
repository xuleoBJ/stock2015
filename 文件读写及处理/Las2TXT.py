# -*- coding: cp936 -*-
import os
import shutil

def las2txt(filePath_forwardLog,filePath_txtLog):
        fileOpened_LasLog=open(filePath_forwardLog,'r')
        fileWrited_txtLog=open(filePath_txtLog.replace(".las",".txt"),'w')
        lineIndex=0
        flag=0
        logSerial=[] 
        for line in fileOpened_LasLog.readlines():
            lineIndex+=1
            if line.startswith('~Curve'):
                flag=1
            if line.startswith('~Ascii'):
                flag=2
            if  flag==1 and (not (line.startswith('~') or line.startswith('#') )):
                splitLine=line.split()
                logSerial.append(splitLine[0])      
            if  flag==2 :
                temp='\t'.join(logSerial)
                fileWrited_txtLog.write(temp+'\n')
                flag=3
            if  flag==3 and (not (line.startswith('~') or line.startswith('#') )):
                fileWrited_txtLog.write(line.strip()+'\n')

        fileWrited_txtLog.close()
        print(filePath_forwardLog+"convert to txtlog complete.")
    
    
if __name__=="__main__":
    
    sourceDirPath="log_las"
    goalDirPath='log_txt'
    
    print ('prepare las to ',goalDirPath)
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)

    ##  把操作目录下文件存入filenameslist
    fileNames=os.listdir(sourceDirPath)
    for wellItem in fileNames:
        print ('Las2txt...'+'-'*10,wellItem)
        fileOpened=sourceDirPath+'\\'+wellItem
        fileWrited=goalDirPath+'\\'+wellItem
        las2txt(fileOpened,fileWrited)
        

    print("处理完毕")
