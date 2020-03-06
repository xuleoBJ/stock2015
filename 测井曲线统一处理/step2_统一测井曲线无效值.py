#-*- coding:utf-8 -*-
import os
import shutil
INVALID_VALUE="-999"

if __name__=="__main__":
    ##测井文件存放目录
    logFileDir=u"logDeal"
    resultPath=u'log_txt_ex_valid'
    if os.path.exists(resultPath):
        shutil.rmtree(resultPath)
    os.mkdir(resultPath)
        
    fileNames=os.listdir(logFileDir)

    for wellLogFile in fileNames:
        print ('-'*10,'Current deal...'+wellLogFile)
        fileOpened=open(logFileDir+'\\'+wellLogFile,'r')
        fileWrited=open(resultPath+'\\'+wellLogFile.lower(),'w')
        lineIndex=0
        seriersIndex=[]
        for line in fileOpened.readlines():
            lineIndex+=1
            splitLine=line.split()
            if lineIndex>1:
                for i in range(0,len(splitLine)):
                    try:
                        if float(splitLine[i])<-500:
                            splitLine[i]=INVALID_VALUE
                    except:
                        pass
            line='\t'.join(splitLine)+'\n'
            fileWrited.write(line)

    fileWrited.close()
