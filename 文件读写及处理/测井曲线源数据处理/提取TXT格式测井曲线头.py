# -*- coding: cp936 -*-
import os
import shutil


##  请把测井格式调整成TXT格式，放在sourceDirPath目录下，
sourceDirPath="111"
fileWritedPath="wellNameAndWelllogSeriers.txt"
fileWrited=open(fileWritedPath,"w")



##  把操作目录下文件存入filenameslist
filenames=os.listdir(sourceDirPath)
logSeriersName=[]
for fileItem in filenames:
    fopen=open(sourceDirPath+'\\'+fileItem,"r")
    print("正在处理。。。"+sourceDirPath+fileItem)
    lineIndex=0
    for line in fopen.readlines():
        lineIndex+=1
        splitLine=line.split()
        if lineIndex==1:
            for item in splitLine:
                logSeriersName.append(item)
            fileWrited.write(fileItem.replace(".txt","")+"    "+line+"\n")
        else:
            break
    fopen.close()

fileWrited.close()
print(set(logSeriersName))
print("处理完毕，文件"+fileWritedPath)


