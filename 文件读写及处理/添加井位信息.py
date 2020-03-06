# -*- coding: cp936 -*-
import os

if __name__=="__main__":

##    print("当前工作路径：",os.getcwd())


    wellName=os.path.basename(os.getcwd())
    print ('Current WellName...'+wellName)
    fileName_wellHead="changed\\wellhead20131018.txt"
    fileName_NeedDeal="changed\\jh_need2.txt"
    openFileWrite="addWellHead.txt"


    fileOpened_wellHead_dic=open(fileName_wellHead,'r')
    fileOpend_NeedDealJH=open(fileName_NeedDeal,'r')
    fileWrited=open(openFileWrite,'w')

    welllName_list=[]
    KB_list=[]
    X_list=[]
    Y_list=[]
    lineZone_list=[]
    

    
    for lineZone in fileOpened_wellHead_dic.readlines():
        if lineZone!="":
            lineZone_list.append(lineZone)
            splitlineZone=lineZone.split()
            welllName_list.append(splitlineZone[0])        
            X_list.append(splitlineZone[1])
            Y_list.append(splitlineZone[2])
            KB_list.append(splitlineZone[3])

   
    lineIndex=0
    lineFlag=1

    for lineLayer in fileOpend_NeedDealJH.readlines():
        if lineLayer!="":
            lineIndex+=1
            print(lineIndex)
            splitLine=lineLayer.split()
            originalValue=0
            if lineIndex>1:
                jh=splitLine[0]
                for i in range(1,len(X_list)):
                    if   welllName_list[i]==jh :
                        splitLine.append(X_list[i])
                        splitLine.append(Y_list[i])
                        splitLine.append(KB_list[i])
                        lineLayer='\t'.join(splitLine)+'\n'
            fileWrited.write(lineLayer)

    fileWrited.close()
    
