# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据同名累加资料：')
    
    fileName_original="cl.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="cl_new.txt"
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
  
    for xcm in set(sList1):
        sumCL=0
        for i in range(len(sList1)):
            if sList1[i]==xcm:
                sumCL=sumCL+float(sList2[i])
        fileWrited.write(xcm+"\t"+str(sumCL)+"\n")
       
    fileOpened_original.close()    
    fileWrited.close()
    print ('OK.')
    
