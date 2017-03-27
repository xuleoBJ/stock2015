# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据解释结论和砂厚算有效厚度：')
    
    fileName_original="jsjl1116.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="jsjl1106_final.txt"
    fileWrited=open(openFileWrite,'w')
    iLine=0
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        line=line.replace("\n","")
        splitline=line.split('\t')
        print(iLine,len(splitline))
        if line!="" and iLine>1:
            sh=float(splitline[3])
            jsjl=splitline[8]
            yxhd=0
            if jsjl=="1":
                yxhd=sh
            elif jsjl in ["5","6","11","8","10"] :
                yxhd=sh*0.5
            splitline.append(str(yxhd))
        fileWrited.write('\t'.join(splitline)+"\n")
    fileOpened_original.close()

     
    
    fileWrited.close()
    print ('OK.')
    
