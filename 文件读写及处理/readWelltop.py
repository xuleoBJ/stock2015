#-*- coding:utf-8 -*-
import os
import sys
##无效值
VALUE_INVALID=-999


##返回 wellTop_listDict keys 'wellName_sList' 'layerName_sList' 'topDepth_fList' 'bottomDepth_fList'
def readFile_geo_wellTop(filepath_wellTop):
    ##存储分层数据
    wellName_wellTop_strList=[]  ##str
    layerName_wellTop_strList=[]  ##str
    topDepth_wellTop_floatList=[]  ##float 
    bottomDepth_wellTop_floatList=[]  ##float
    lineIndex=0
    for line in open(filepath_wellTop,'r').readlines():
         lineIndex= lineIndex+1
         splitLine=line.split()
         if line!="" and len(splitLine)>=4 and lineIndex>1:
            jh_str=splitLine[0]
            layerName_str=splitLine[1]
            try:
                topDepth_float=float(splitLine[2])
                bottomDepth_float=float(splitLine[3])
                if bottomDepth_float<=topDepth_float:##比较底深是否小于顶深
                    print("顶底深有误---"+line)
                if len(wellName_wellTop_strList)>1 and jh_str==wellName_wellTop_strList[-1]:
                    ##比较顶深是否小于本井上个底深
                    if topDepth_float<bottomDepth_wellTop_floatList[-1]:
                        print(topDepth_float,bottomDepth_wellTop_floatList[-1],"与上个顶底数据矛盾---"+line)
            except:
                print(filepath_wellTop+' has mistakes in '+line)
                sys.exit(0)
            wellName_wellTop_strList.append(jh_str)
            layerName_wellTop_strList.append(layerName_str)
            topDepth_wellTop_floatList.append(topDepth_float)
            bottomDepth_wellTop_floatList.append(bottomDepth_float)
    wellTop_listDict={}
    wellTop_listDict['wellName_sList']=wellName_wellTop_strList
    wellTop_listDict['layerName_sList']=layerName_wellTop_strList
    wellTop_listDict['topDepth_fList']=topDepth_wellTop_floatList
    wellTop_listDict['bottomDepth_fList']=bottomDepth_wellTop_floatList
    
    print("完成分层数据读取。")
    return(wellTop_listDict)



    
if __name__=="__main__":
    print("读取分层数据-------数据格式： \n 井名，小层名，小层顶深 ，小层底深")
    filepath_wellTop="data\wellTop.txt"
    wellTop_listDict=readFile_geo_wellTop(filepath_wellTop)
    print(wellTop_listDict)



    
    

 

    
