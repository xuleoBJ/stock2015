# -*- coding: cp936 -*-
import os
import shutil


##  ��Ѳ⾮��ʽ������TXT��ʽ������sourceDirPathĿ¼�£�
sourceDirPath="111"
fileWritedPath="wellNameAndWelllogSeriers.txt"
fileWrited=open(fileWritedPath,"w")



##  �Ѳ���Ŀ¼���ļ�����filenameslist
filenames=os.listdir(sourceDirPath)
logSeriersName=[]
for fileItem in filenames:
    fopen=open(sourceDirPath+'\\'+fileItem,"r")
    print("���ڴ�������"+sourceDirPath+fileItem)
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
print("������ϣ��ļ�"+fileWritedPath)


