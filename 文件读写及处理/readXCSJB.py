#-*- coding:utf-8 -*-
import os
import sys
##无效值
VALUE_INVALID=-999

##存储分层数据
wellName_wellTop_strList=[]  ##str
layerName_wellTop_strList=[]  ##str
X_wellTop_floatList=[]  ##float 
Y_wellTop_floatList=[]  ##float 
topDepth_wellTop_floatList=[]  ##float 
bottomDepth_wellTop_floatList=[]  ##float
topElevation_wellTop_floatList=[]  ##float
bottomElevation_wellTop_floatList=[]  ##float
layerThickness_wellTop_floatList=[]##float
sandThickness_wellTop_floatList=[]##float
por_wellTop_floatList=[]##float
per_wellTop_floatList=[]##float
so_wellTop_floatList=[]##float

def readFile_geo_wellTop(filepath_wellTop):
    lineIndex=0
    for line in open(filepath_wellTop,'r').readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
            splitLine=line.split()
            jh_str=splitLine[0]
            layerName_str=splitLine[1]
            try:
                topDepth_float=float(splitLine[2])
                bottomDepth_float=float(splitLine[3])

                if bottomDepth_float<=topDepth_float:##比较底深是否小于顶深
                    print(u"顶底深有误---"+line)
                if len(wellName_wellTop_strList)>1 and jh_str==wellName_wellTop_strList[-1]:
                    ##比较顶深是否小于本井上个底深
                    if topDepth_float<bottomDepth_wellTop_floatList[-1]:
                        print(topDepth_float,bottomDepth_wellTop_floatList[-1],u"与上个顶底数据矛盾---"+line)
            except:
                print(u"顶底深有误---"+line)
                sys.exit(0)
            wellName_wellTop_strList.append(jh_str)
            layerName_wellTop_strList.append(layerName_str)
            topDepth_wellTop_floatList.append(topDepth_float)
            bottomDepth_wellTop_floatList.append(bottomDepth_float)
            X_wellTop_floatList.append(VALUE_INVALID) ##float
            Y_wellTop_floatList.append(VALUE_INVALID) ##float
            topElevation_wellTop_floatList.append(VALUE_INVALID) ##float
            bottomElevation_wellTop_floatList.append(VALUE_INVALID) ##float
            layerThickness_wellTop_floatList.append(VALUE_INVALID)##float
            sandThickness_wellTop_floatList.append(VALUE_INVALID)##float
            por_wellTop_floatList.append(VALUE_INVALID)##float
            per_wellTop_floatList.append(VALUE_INVALID)##float
            so_wellTop_floatList.append(VALUE_INVALID)##float
    print("完成分层数据读取。")

if __name__=='__main__':
    print("读取分层数据-------数据格式： \n 井名，小层名，小层顶深 ，小层底深")
    filepath_wellTop=u"testData\wellTop.txt"
    readFile_geo_wellTop(filepath_wellTop)
    


    
    

 

    
