# -*- coding: cp936 -*-
import os
import shutil

def calTk(stl): ## ������͸��ͻ��ϵ�� �����͸����ɰ��ƽ����͸�ʵı�ֵ��
    stl=map(float,stl)
    return round(max(stl)/(sum(stl)/len(stl)),3)

def calJk(stl): ## ������͸�ʼ��� �����͸������Сֵ�ı�ֵ��
    stl=map(float,stl)
    return round(max(stl)/min(stl),3)

def calVk(stl):
     stl=map(float,stl)
     stl_avg=sum(stl)/len(stl)
     SD=0 ##Standard deviations
     for item in stl:
         SD=SD+(item-stl_avg)**2
     SD=SD/len(stl)
     return round(SD**0.5/stl_avg,3)

if __name__=="__main__":
    fileItem="demo.txt"
    fileOpened=open(fileItem,'r')
    lineIndex=0

    ##xx���ļ�������͸����ֵ������xx�ַ�����List��
    xx=[]
    for line in fileOpened.readlines():
        lineIndex+=1
        splitLine=line.split()
        xx.append(splitLine[1])

##    xx=[1,2,3,4,5]
    Tk=calTk(xx)
    Jk=calJk(xx)
    Vk=calVk(xx)
    _result=""
    if Vk<0.5:
         _result="low-heterogeneous"
    elif 0.5<=Vk<=0.7:
        _result="mid-heterogeneous"
    elif Vk>=0.7:
        _result="high-heterogeneous"
    print(Tk,Jk,Vk,_result)

##    sourceDirPath="log_txt"
##    goalFilePath='�Ǿ��ʷ���.txt'
##    fileWrited=open(goalFilePath,'w')
##
##    fileNames=os.listdir(sourceDirPath)
##    for fileItem in fileNames:
##        print ('-'*10,'Current dealing...'+fileItem)
##        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
##        lineIndex=0
##        for line in fileOpened.readlines():
##            lineIndex=lineIndex+1
##            if  lineIndex>1:
##                splitline=line.split()
##                if (float(splitline[1])<=0.001 or float(splitline[2])<=0):
##                    print(lineIndex)
##                    pass
##                else:
##                    fileWrited.write(fileItem.replace(".txt",'\t')+line)
##            if  lineIndex==1:
##                    fileWrited.write("����\t"+line)
##    fileWrited.close()
##    print("���ļ��ڡ���"+goalFilePath)
