# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('根据解释结论和砂厚算有效厚度：')
    
    fileName_original="stl_bhd.txt"
    fileOpened_original=open(fileName_original,'r')

    openFileWrite="stl_new.txt"
    fileWrited=open(openFileWrite,'w')
    iLine=0
    for line in fileOpened_original.readlines():
        iLine=iLine+1
        splitline=line.strip().split()
        stl=float(splitline[0])
        bhd=float(splitline[1])
        jsjl=int(splitline[2])
        if bhd>100:
            splitline.append(str(bhd))
            splitline.append("-999")
        elif bhd>50 and jsjl!=1:
            splitline.append(str(stl))
            splitline.append(str(100-bhd))
        else:
            splitline.append(str(stl))
            splitline.append(str(bhd))
            
        
        fileWrited.write('\t'.join(splitline)+"\n")

     
    
    fileWrited.close()
    print ('OK.')
    
