# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据条件筛选资料：')
    
    fileName_original="singleLine.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="singleLine_new.txt"
    fileWrited=open(openFileWrite,'w')
    sList1=[]
    sList2=[]
    iLine=0
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        if line!="":
            splitline=line.split()
            print iLine
            sList1.append(splitline[0])
            sList2.append(splitline[1])
  
    for i in range(1,len(sList1)):
        f1=float(sList1[i])
        f2=float(sList2[i])
        if f1-f2>700:
            sList1[i]=str(f2-10)
        fileWrited.write(sList1[i]+"\t"+sList2[i]+"\n")
    fileOpened_original.close()    
    fileWrited.close()
    print ('OK.')
    
