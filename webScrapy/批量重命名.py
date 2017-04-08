import os
import shutil


if __name__=="__main__":

    sourceDirPath="H:\\mp3\\秦朔朋友圈"

    

    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        if fileItem.endswith(".mp3"):
            newFileName = sourceDirPath+'\\'+fileItem.replace("mp3","m4a")
            originalFileName=sourceDirPath+'\\'+fileItem
            os.rename(originalFileName,newFileName,True
