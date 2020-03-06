# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据解释结论和砂厚算有效厚度：')
    
    fileName_original="hd.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="hd_new.txt"
    fileWrited=open(openFileWrite,'w')
    iLine=0
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        splitline=line.strip().split()
        hd1=float(splitline[0])
        hd2=float(splitline[1])
        splitline.append(str(hd2-hd1))
            
        
        fileWrited.write('\t'.join(splitline)+"\n")
##        if line!="" and iLine>1:
##            sh=float(splitline[2])
##            print iLine
##            if sh>0:
##                 fileWrited.write('\t'.join(splitline)+"\n")
    fileOpened_original.close()

     
    
    fileWrited.close()
    print ('OK.')
