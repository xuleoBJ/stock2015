# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据解释结论和砂厚算有效厚度：')
    
    fileName_original="jsjl1103.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="jsjl1103_new.txt"
    fileWrited=open(openFileWrite,'w')
    iLine=0
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        splitline=line.strip().split()
        kxd1=float(splitline[0])
        kxd2=float(splitline[1])
        if kxd1>kxd2:
            if kxd2>60:
                kxd2=100-kxd2
            splitline.append(str(kxd2))
        else:
            if kxd1>60:
                kxd1=100-kxd1
            splitline.append(str(kxd1))
            
        
        fileWrited.write('\t'.join(splitline)+"\n")
##        if line!="" and iLine>1:
##            sh=float(splitline[2])
##            print iLine
##            if sh>0:
##                 fileWrited.write('\t'.join(splitline)+"\n")
    fileOpened_original.close()

     
    
    fileWrited.close()
    print ('OK.')
