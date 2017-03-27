# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据条件筛选资料：')
    
    fileName_original="100-2"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite=fileName_original+"_new.txt"
    fileWrited=open(openFileWrite,'w')
    sList=[]
    iLine=0
    
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        if line!="" and iLine>=7 and iLine%2==1:
            sList.append(line)
  
    fileWrited.write("井深 垂深 斜度 方位 真方位 总方位 总位移 E坐标 N坐标 \n")
    for line in sList:
        split=line.split()
        del split[0]
        fileWrited.write("\t".join(split)+"\n")
    fileOpened_original.close()    
    fileWrited.close()
    print ('OK.')
    
