# -*- coding: cp936 -*-
import os
import shutil
if __name__=="__main__":
    
    sourceDirPath="C���ֵ��"
    goalDirPath=sourceDirPath+"4petrel"
    
    print ('prepare ��ֵ�� ',goalDirPath)
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)

    ##  �Ѳ���Ŀ¼���ļ�����filenameslist
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('forward2txt...'+'-'*10,fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        fileWrited=open(goalDirPath+'\\'+fileItem,'w')
        lineIndex=0
        n=0
        for line in fileOpened.readlines():
            lineIndex+=1
            if lineIndex>1:
                splitLine=line.split()
                if len(splitLine)==2:
                    _value=splitLine[1]
                    n=n+1
                if len(splitLine)==3:
                    
                    fileWrited.write(splitLine[0]+'\t'+splitLine[1]+'\t'+str(n)+'\t'+_value+'\n')
            
    fileWrited.close()
    print("�������")
