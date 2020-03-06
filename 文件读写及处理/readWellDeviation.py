#-*- coding:utf-8 -*-
import os
import sys

def readFile_geo_wellDeviation2list_1(filepath_wellPath):##格式wellname，md（float），inclination()，azimuth（float）
    wellPathInfor_list=[] ##list[list], 每个list 包括wellname，md（float），inclination()，azimuth（float）
    fileOpened_wellPath=open(filepath_wellPath,'r')
    lineIndex=0
    for line in fileOpened_wellPath.readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
            print("需要编写")
    return wellPathInfor_list

def readFile_geo_wellDeviation2list_2(filepath_wellPath): ##格式wellname，TVD（float），DX，DY
    wellPathInfor_list=[] ##list[list], 每个list 包括
    fileOpened_wellPath=open(filepath_wellPath,'r')
    lineIndex=0
    for line in fileOpened_wellPath.readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
             print("需要编写")
    return wellPathInfor_list


def readFile_geo_wellPath2dict(filepath_wellPath):##格式wellname，md（float），inclination()，azimuth（float）
    wellPathInfor_dict={} 
    wellName_sList=[]
    md_fList=[]
    x_fList=[]
    y_fList=[]
    fileOpened_wellPath=open(filepath_wellPath,'r')
    lineIndex=0
    for line in fileOpened_wellPath.readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
            splitline=line.split()
            if len(splitline)>=4:
                wellName_sList.append(splitline[0])
                md_fList.append(float(splitline[1]))
                x_fList.append(float(splitline[2]))
                y_fList.append(float(splitline[3]))
                
            else:
                print(filepath_wellPath+'has mistakes in'+line)
    
    wellPathInfor_dict['wellName_sList']=wellName_sList
    wellPathInfor_dict['x_fList']=x_fList
    wellPathInfor_dict['y_fList']=y_fList
    wellPathInfor_dict['md_fList']=md_fList
    return wellPathInfor_dict   

if __name__=='__main__':
    wellPathInfor_dict=readFile_geo_wellPath2dict("testData\wellPath.txt")
    print wellPathInfor_dict['wellName_sList']

    print("完成井头数据读取。")
    
    


    
    

 

    
