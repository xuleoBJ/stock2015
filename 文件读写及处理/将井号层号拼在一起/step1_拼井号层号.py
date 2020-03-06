# -*- coding: cp936 -*-
import os

if __name__=="__main__":

##    print("当前工作路径：",os.getcwd())


    wellName=os.path.basename(os.getcwd())
    print ('将井行、层号拼在一起，形成备用文件：')
    fileName_wellNameList="jh.txt"
    fileName_layerSeriers="xcm.txt"
    openFileWrite="wellName_layer_xl.txt"



    fileOpenedWellNameList=open(fileName_wellNameList,'r')
    fileOpenedLayerSeriers=open(fileName_layerSeriers,'r')
    fileWrited=open(openFileWrite,'w')


    welllName_list=[]
    layerSeriers_list=[]
    for lineLayer in fileOpenedLayerSeriers.readlines():
        if lineLayer!="":
            splitline=lineLayer.split()
            layerSeriers_list.append(splitline[0]) 

    for lineZone in fileOpenedWellNameList.readlines():
        if lineZone!="":
            splitlineZone=lineZone.split()
            welllName_list.append(splitlineZone[0]) 
   


    for i in range(len(welllName_list)) :
        for j in range(len(layerSeriers_list)):
            fileWrited.write(welllName_list[i]+'\t'+layerSeriers_list[j]+'\n')

    fileWrited.close()
    
