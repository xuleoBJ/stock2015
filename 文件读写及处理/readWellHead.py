#-*- coding:utf-8 -*-
import os
import sys

def readFile_geo_wellhead(filepath_wellHead):
    wellHeadInfor_list=[] ##list[list], 每个list 包括wellname，x（float），y（float），KB
    fileOpened_wellHead=open(filepath_wellHead,'r')
    lineIndex=0
    for lineWellHead in fileOpened_wellHead.readlines():
         lineIndex= lineIndex+1
         if lineWellHead!="" and lineIndex>1:
            wellInfor=[]
            splitlineWellHead=lineWellHead.split()
            wellInfor.append(splitlineWellHead[0])
            wellInfor.append(float(splitlineWellHead[1]))
            wellInfor.append(float(splitlineWellHead[2]))
            wellInfor.append(float(splitlineWellHead[3]))
            wellHeadInfor_list.append(wellInfor)
    return wellHeadInfor_list

def readFile_geo_wellhead2dict(filepath_wellHead):
    wellHeadInfor_dict={} ##list[dict], 每个list 包括wellname，x（float），y（float），KB
    wellName_sList=[]
    x_fList=[]
    y_fList=[]
    kb_fList=[]
    fileOpened_wellHead=open(filepath_wellHead,'r')
    lineIndex=0
    for lineWellHead in fileOpened_wellHead.readlines():
         lineIndex= lineIndex+1
         if lineWellHead!="" and lineIndex>1:
            splitlineWellHead=lineWellHead.split()
            if len(splitlineWellHead)>=4:
                wellName_sList.append(splitlineWellHead[0])
                x_fList.append(float(splitlineWellHead[1]))
                y_fList.append(float(splitlineWellHead[2]))
                kb_fList.append(float(splitlineWellHead[3]))
            else:
                print(filepath_wellHead+'has mistakes in'+lineWellHead)
    
    wellHeadInfor_dict['wellName_sList']=wellName_sList
    wellHeadInfor_dict['x_fList']=x_fList
    wellHeadInfor_dict['y_fList']=y_fList
    wellHeadInfor_dict['kb_fList']=kb_fList
    return wellHeadInfor_dict   

if __name__=='__main__':
    wellHeadInfor_dict=readFile_geo_wellhead2dict("testData\wellHead.txt")
    print wellHeadInfor_dict['wellName_sList']

    print("完成井头数据读取。")
    
    


    
    

 

    
