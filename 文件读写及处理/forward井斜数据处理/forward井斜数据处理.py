# -*- coding: cp936 -*-
import os

if __name__=="__main__":


    print ('��������ɸѡ���ϣ�')
    
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
  
    fileWrited.write("���� ���� б�� ��λ �淽λ �ܷ�λ ��λ�� E���� N���� \n")
    for line in sList:
        split=line.split()
        del split[0]
        fileWrited.write("\t".join(split)+"\n")
    fileOpened_original.close()    
    fileWrited.close()
    print ('OK.')
    
