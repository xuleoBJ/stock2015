# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据解释结论和砂厚算有效厚度：')
    
    fileName_original="jsjl1024.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="1024_del.txt"
    fileWrited=open(openFileWrite,'w')
    iLine=0
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        line=line.replace("\n","")
        splitline=line.split('\t')
##        if len(splitline>=6:
##            fileWrited.write('\t'.join(splitline)+"\n")
        if line!="" and iLine>1:
            sh=float(splitline[2])
            print iLine
            if sh>0:
                 fileWrited.write('\t'.join(splitline)+"\n")
    fileOpened_original.close()

     
    
    fileWrited.close()
    print ('OK.')
    
