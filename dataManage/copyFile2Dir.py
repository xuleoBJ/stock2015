# -*- coding: cp936 -*-
import os
import shutil


if __name__=="__main__":
    
    src="C:\\new_dxzq_v6\\T0002\\export\\" 
    sourceDirPath=src
    stockSelectPath="stockSelect"
       
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
    print("job done")
