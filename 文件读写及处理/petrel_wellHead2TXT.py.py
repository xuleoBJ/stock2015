# -*- coding: cp936 -*-
import os
import shutil

def change2TXT_petrelWellHead(filePath_wellHeadPetrel,filePath_wellHeadTXT):
        fileOpened_forwardLog=open(filePath_wellHeadPetrel,'r')
        fileWrited_txtLog=open(filePath_wellHeadTXT,'w')
        lineIndex=0
        flag=False
        lineHead_sList=[]
        
        for line in fileOpened_forwardLog.readlines():
            splitLine=line.split()
            lineIndex+=1
            if line.startswith("BEGIN") and flag==False:
                flag=True
            elif line.startswith("END "):
                flag=False
            elif flag==True and not line.startswith("END "):
                lineHead_sList.append(splitLine[0])
            else:
                    print('\t'.join(lineHead_sList)+'\t')
        print(filePath_wellHeadPetrel+"convert to txtlog complete.")
    
        fileWrited_txtLog.close()

if __name__=="__main__":
    
    sourceDirPath="testData"
    goalDirPath='wellHead_txt'
    
    print ('prepare  to ',goalDirPath)
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)

    ##  把操作目录下文件存入filenameslist
    fileNames=os.listdir(sourceDirPath)
    for wellItem in fileNames:
        fileOpened=sourceDirPath+'\\'+wellItem
        fileWrited=goalDirPath+'\\'+wellItem
        change2TXT_petrelWellHead(fileOpened,fileWrited)
        

    print("处理完毕")
