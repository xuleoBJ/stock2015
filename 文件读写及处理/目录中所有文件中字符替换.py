# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    sourceDirPath="testData"
    goalDirPath='�滻�ַ����ļ���'
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
            line=line.replace('�;�','3')
            line=line.replace('ˮ��','15')
            line=line.replace('��','d')
            line=line.replace('��','shi')
            line=line.replace('ɰ','sha')
            line=line.replace('Ӣ','y')

            fileWrited.write(line)
    fileWrited.close()
    print("���ļ���"+goalDirPath)
