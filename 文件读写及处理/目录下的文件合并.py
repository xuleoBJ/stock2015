# -*- coding: cp936 -*-
import os
import shutil


if __name__=="__main__":

    sourceDirPath="111"
    goalFilePath='�ϲ��ļ���.txt'
    fileWrited=open(goalFilePath,'w')

    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        for line in fileOpened.readlines():
            fileWrited.write(line)
    fileWrited.close()
    print("���ļ��ڡ���"+goalFilePath)
