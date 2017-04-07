import os
import shutil


if __name__=="__main__":

    sourceDirPath="H:\\迅雷下载"
    goalDir='123'
    

    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        if fileItem.endswith(".m4a"):
            newFileName = sourceDirPath+'\\'+fileItem.replace("m4a","mp3")
            originalFileName=sourceDirPath+'\\'+fileItem
            os.rename(originalFileName,newFileName)
