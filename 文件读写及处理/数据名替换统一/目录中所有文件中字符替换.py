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
            line=line.replace('�;�','3')
            line=line.replace('ˮ��','15')
            line=line.replace('��','d')
            line=line.replace('��','shi')
            line=line.replace('ɰ','sha')
            line=line.replace('Ӣ','y')
            line=line.replace('̽','tan')
            line=line.replace('��','xin')
            line=line.replace('�ϵ�','fault')
            line=line.replace('����','YX')
            line=line.replace('�Ͷ�','YD')
            line=line.replace('�ϵ�','Fault')

            line=line.replace('�����Ͳ�','13')
            line=line.replace('����ˮ��','10')
            line=line.replace('����ˮ��','11')
            line=line.replace('��ˮͬ��','6')
            line=line.replace('������','9')
            line=line.replace('��������','8')
            line=line.replace('���Ͳ�','11')

            line=line.replace('����ͬ��','5')
            line=line.replace('������','5')
            line=line.replace('��ˮͬ��','7')
            line=line.replace('���ɲ�','13')
            line=line.replace('ú��','12')
            line=line.replace('�Ͳ�','1')
            line=line.replace('ˮ��','2')
            line=line.replace('����','3')
            line=line.replace('�ɲ�','4')
            line=line.replace('����','0')
            



    
            
            fileWrited.write(line)
    fileWrited.close()
    fileOpened.close()
    print("���ļ���"+goalDirPath)
