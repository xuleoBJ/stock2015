# -*- coding: cp936 -*-
import os
import shutil


##  ��Ѳ⾮��ʽ������TXT��ʽ���޸�Ŀ¼��
dirPathLogFilesTxt="log_txt"
fileWritedPath="wellNameAndWelllogSeriers.txt"
fileWrited=open(fileWritedPath,"w")

##  �Ѳ���Ŀ¼���ļ�����filenameslist
logSeriersName=[]
for fileItem in os.listdir(dirPathLogFilesTxt):
    fopen=open(dirPathLogFilesTxt+'\\'+fileItem,"r")
    print("���ڴ�������"+dirPathLogFilesTxt+fileItem)
    lineIndex=0
    for line in fopen.readlines():
        lineIndex+=1
        splitLine=line.split()
        if lineIndex==1:
            for item in splitLine:
                logSeriersName.append(item)
            fileWrited.write(fileItem.replace(".txt","\t")+'\t'.join(splitLine)+"\n")
        else:
            break
    fopen.close()

fileWrited.close()
print(set(logSeriersName))
print("������ϣ��ļ�"+fileWritedPath)


