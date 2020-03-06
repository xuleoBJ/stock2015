# -*- coding: cp936 -*-
import os
import shutil

if __name__=="__main__":

    sourceDirPath="118"
    goalDirPath='118changed'
    if os.path.exists(goalDirPath):
        shutil.rmtree(goalDirPath)
    os.mkdir(goalDirPath)
        
    fileNames=os.listdir(sourceDirPath)

    for fileItem in fileNames:
        print ('-'*10,'Current dealing...'+fileItem)
        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
        fileWrited=open(goalDirPath+'\\'+fileItem.lower(),'w')
        lineIndex=0
        for line in fileOpened.readlines():
##            print line
            lineIndex+=1
            line=line.replace('油井','3')
            line=line.replace('水井','15')
            line=line.replace('东','d')
            line=line.replace('试','shi')
            line=line.replace('砂','sha')
            line=line.replace('英','y')
            line=line.replace('探','tan')
            line=line.replace('新','xin')
            line=line.replace('断点','fault')
            line=line.replace('油下','YX')
            line=line.replace('油断','YD')
            line=line.replace('断点','Fault')

            line=line.replace('可疑油层','13')
            line=line.replace('含油水层','10')
            line=line.replace('含气水层','11')
            line=line.replace('油水同层','6')
            line=line.replace('差气层','9')
            line=line.replace('差油气层','8')
            line=line.replace('差油层','11')

            line=line.replace('油气同层','5')
            line=line.replace('油气层','5')
            line=line.replace('气水同层','7')
            line=line.replace('可疑层','13')
            line=line.replace('煤层','12')
            line=line.replace('油层','1')
            line=line.replace('水层','2')
            line=line.replace('气层','3')
            line=line.replace('干层','4')
            line=line.replace('其它','0')
            



    
            
            fileWrited.write(line)
    fileWrited.close()
    fileOpened.close()
    print("新文件在"+goalDirPath)
