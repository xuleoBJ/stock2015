# -*- coding: cp936 -*-
import os
import shutil
import datetime


fileWritedHeadline=open("headline.txt",'w')
def las2txt(filePath_forwardLog,filePath_txtLog):
        fileOpened_LasLog=open(filePath_forwardLog,'r')
        fileWrited_txtLog=open(filePath_txtLog.lower().replace(".las",".txt"),'w')
        lineIndex=0
        flag=0
        logSeriesList=[]
        firstMeet = 1  ## 标志第一空行不写
        numOfseriers = 0
        valueList =[]
        for line in fileOpened_LasLog.readlines():
            lineIndex+=1
            if flag==1 and line.startswith('~'): ##结束读取~c段
                flag=4
            if line.startswith('~C'): ##开始读取~c段
                flag=1
            if  flag==1 and (not (line.startswith('~') or line.startswith('#') )): ##写Headline
                splitLine=line.split()
                logSeriesList.append(splitLine[0])      

            if line.startswith('~A'):  #开始写数据
                flag=2
            if  flag==2 :  #开始写测井系类头数据
                temp='\t'.join(logSeriesList)
                fileWrited_txtLog.write(temp+'\n')
                flag=3
                numOfseriers = len(logSeriesList)
          
            if  flag==3 and (not (line.startswith('~') or line.startswith('#') )): #开始写数据行
                splitLine=line.split()
                valueList.extend(splitLine)
                if len(valueList) == numOfseriers:
                    fileWrited_txtLog.write('\t'.join(valueList)+'\n')
                    valueList=[]

        fileWritedHeadline.write(os.path.basename(filePath_forwardLog)+"\t"+'\t'.join(logSeriesList)+"\n")
        fileWrited_txtLog.close()
        print(filePath_forwardLog+"convert to txtlog complete.")
    
    
if __name__=="__main__":
    starttime = datetime.datetime.now()

    
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
        
    fileWritedHeadline.close()
    #long running
    endtime = datetime.datetime.now()
    print ("耗时(秒):" + str((endtime - starttime).seconds))
    print("处理完毕")
