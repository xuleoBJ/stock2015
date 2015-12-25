# -*- coding: cp936 -*-
import os
import shutil
import Ccomfunc

def copyData2Dir():
    sourceDirPath=Ccomfunc.src
    stockSelectPath=Ccomfunc.dirData
       
    if not os.path.exists(stockSelectPath):
        os.makedirs(stockSelectPath)
    
    stockMarketIDList=["999999","399001"]
    stockSelectIDList=["002001","600178"]
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('-'*5+'Current copying:\t'+fileItem)
        filePathSource=sourceDirPath+'\\'+fileItem
        if os.path.splitext(fileItem)[0] in stockMarketIDList+stockSelectIDList:
            fileoPathGoal=stockSelectPath+"\\"+fileItem
            shutil.copyfile(filePathSource,fileoPathGoal)

if __name__=="__main__":
    copyData2Dir()
    print("job done")
