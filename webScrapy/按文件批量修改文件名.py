
import os
import shutil


if __name__=="__main__":

    sourceDirPath="H:\\迅雷下载"
    fileNameText="H:\\迅雷下载\\33943825.txt"
    fileOpened=open(fileNameText,'r')
    nameListChinese=[]
    nameListEnglish=[]
    for line in fileOpened.readlines():
        splitLine = line.split()
        nameListChinese.append(splitLine[1])
        nameListEnglish.append(splitLine[2])
    fileOpened.close()
    fileNames=os.listdir(sourceDirPath)
   # print(nameListEnglish)
    for fileItem in fileNames:
        for i in range(len(nameListEnglish)):
            codeName = fileItem[:-4]
            if codeName in nameListEnglish[i] :
                print(os.path.basename(nameListChinese[i]))
                print ('-'*10,'Current dealing...'+fileItem)
                newFileName = sourceDirPath+'\\'+fileItem.replace(codeName,nameListChinese[i])
                originalFileName=sourceDirPath+'\\'+fileItem
                os.rename(originalFileName,newFileName)
                break
