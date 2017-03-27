# -*- coding: cp936 -*-
import os
DataStartNumber=1  ## 数据起始行，如果有标题行，DataStartNumber=1

WellNameColumnNumber=0 ## 数据列，从0开始
XColumnNumber=0
YColumnNumber=0
TopDepthColumnNumber=1
BottomDepthColumnNumber=2
LayerNameColumnNumber=3
LayerThicknessColumnNumber=4
SandThicknessColumnNumber=5
PoreColumnNumber=6
PermColumnNumber=7
SoColumnNumber=8
InterpretationColumnNumber=9

if __name__=="__main__":

    print("正在对小层数据表进行数据校正调整：",os.getcwd())

 
    filepath_xcsjb="小层数据1112.txt"
##    print ('Current WellName...'+wellName)
##    fileName_xcsjb=filepath_xcsjb
    openFileWrite="_update_"+filepath_xcsjb


    fileZoneOpened=open(filepath_xcsjb,'r')
    fileWrited=open(openFileWrite,'w')

    jh_list=[]
    zoneName_list=[]
    dingShen_list=[]
    diShen_list=[]
    lineZone_list=[]
    
    lineLayerIndex=0
    
    for lineZone in fileZoneOpened.readlines():
        
         lineLayerIndex= lineLayerIndex+1
         
         if lineZone!="" and lineLayerIndex>DataStartNumber:
            lineZone_list.append(lineZone)
            splitlineZone=lineZone.split()
            jh_list.append(splitlineZone[WellNameColumnNumber])
            zoneName_list.append(splitlineZone[LayerNameColumnNumber])
            dingShen_list.append(splitlineZone[TopDepthColumnNumber])
            diShen_list.append(splitlineZone[BottomDepthColumnNumber])
##            kxd_list.append(splitlineZone[PoreColumnNumber])
            
    for i in range(len(jh_list)-1):
        if jh_list[i]== jh_list[i+1]:
            fileWrited.write(lineZone_list[i])
            splitlineLayer=lineZone_list[i].split()

            if dingShen_list[i+1]!=diShen_list[i]:
##                print(len(splitlineLayer))
                splitlineLayer[1]=diShen_list[i]
                splitlineLayer[2]=dingShen_list[i+1]
                splitlineLayer[3]='0'
                fileWrited.write('\t'.join(splitlineLayer)+'\n')
                
    fileWrited.close()
    
