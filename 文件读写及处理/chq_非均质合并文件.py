# -*- coding: cp936 -*-
import os
import shutil


if __name__=="__main__":

    sourceDirPath="log_txt"
    goalFilePath='非均质分析.txt'
    fileWrited=open(goalFilePath,'w')

    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex=lineIndex+1
            if  lineIndex>1:
                splitline=line.split()
                if (float(splitline[1])<=0.001 or float(splitline[2])<=0):
                    print(lineIndex)
                    pass
                else:
                    fileWrited.write(fileItem.replace(".txt",'\t')+line)
            if  lineIndex==1:
                    fileWrited.write("井号\t"+line)
    fileWrited.close()
    print("新文件在——"+goalFilePath)
