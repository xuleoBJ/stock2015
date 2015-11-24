# -*- coding: cp936 -*-
import os
import shutil


if __name__=="__main__":
    
    src="C:\\new_dxzq_v6\\T0002\\export\\" 
    dst='dataStock'
    src2dst=False
    if src2dst==True:
        sourceDirPath=src
        goalDirPath=dst
    else:
        sourceDirPath=dst
        goalDirPath=src
    if not os.path.exists(goalDirPath):
        os.makedirs(goalDirPath)
    
    stockIDList=["999999","399001","002001","600178"]
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        if os.path.splitext(fileItem)[0] in stockIDList:
            print ('-'*5+'Current copying:\t'+fileItem)
            filePathSource=sourceDirPath+'\\'+fileItem
            fileoPathGoal=goalDirPath+"\\"+fileItem
            shutil.copyfile(filePathSource,fileoPathGoal)
    print("job done")
