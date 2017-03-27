#-*- coding:utf-8 -*-
import os
import sys
##无效值
VALUE_INVALID=-999

def readFile_geo_layerName(filepath_layerName):
    fileOpened_layerName=open(filepath_layerName,'r')
    layerName_strList=[]
    lineIndex=0
    for line in fileOpened_layerName.readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
            splitLine=line.split()
            layerName_strList.append(splitLine[0])
    print("完成地层名读取。")
    return(layerName_strList)

if __name__=='__main__':
    print("读取层位数据，请注意按照从上到下的顺序-------")
    filepath_layerName=u"testData\layerName.txt"
    print(readFile_geo_layerName(filepath_layerName))
    


    
    

 

    
