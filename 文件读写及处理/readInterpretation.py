#-*- coding:utf-8 -*-
import os
import sys

##存储解释成果表
wellName_interpretation_strList=[]  ##str
topDepth_interpretation_floatList=[]  ##float 海拔
bottomDepth_interpretation_floatList=[]  ##float 海拔
interpretationThickness_interpretation_floatList=[] ##float
sandThickness_interpretation_floatList=[]  ##float 海拔
por_interpretation_floatList=[]
per_interpretation_floatList=[]
so_interpretation_floatList=[]
interpretationResult_interpretation_strList=[]

def readFile_geo_interpretationData(filepath_interpretationData):
    lineIndex=0
    for line in open(filepath_interpretationData,'r').readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
            splitLine=line.split()
            jh=splitLine[0]
            try:       ##判断顶深
                dingshen=float(splitLine[1]) ##float
            except:
                print(u"井名"+jh+"顶深有错误")
                sys.exit(0)
            try:    ##判断顶深
                dishen=float(splitLine[2])
                if dishen<=dingshen:
                    print("下面行底深有错误---"+line)
                    effInforWrited("下面行底深有错误---"+line)
            except:
                print("下面行底深有错误---"+line)
                effInforWrited("下面行底深有错误---"+line)
                sys.exit(0)
            jieshiHD=float(splitLine[3])
            yxhd=float(splitLine[4]) 
            try :  ##判断pore值的有效性，超过值域用系统无效值
                kxd=float(splitLine[5])
                if 0>=kxd and kxd>=50:
                    kxd=VALUE_INVALID
            except:
                print(line+"孔隙度有错误")
                sys.exit(0)
            try :  ##判断per值的有效性，超过值域用系统无效值
                stl=float(splitLine[6])
                if 0>=stl :
                    stl=VALUE_INVALID
            except:
                print(line+"渗透率有错误")
                sys.exit(0)

            try :  ##判断so值的有效性，超过值域用系统无效值
                so=float(splitLine[7])
                if so>90 :
                    stl=VALUE_INVALID
            except:
                print(line+"饱和度有错误")
                sys.exit(0)
            if len(splitLine)>8: ##判断是否有解释结论，没有用空值
                jsjl=splitLine[8]
            else:
                jsjl=""
            wellName_interpretation_strList.append(jh)
            topDepth_interpretation_floatList.append(dingshen)
            bottomDepth_interpretation_floatList.append(dishen)
            interpretationThickness_interpretation_floatList.append(jieshiHD)
            sandThickness_interpretation_floatList.append(yxhd)   
            por_interpretation_floatList.append(kxd)
            per_interpretation_floatList.append(stl)
            so_interpretation_floatList.append(so)
            interpretationResult_interpretation_strList.append(jsjl)
    print("完成解释成果表数据读取。") 

if __name__=='__main__':
    print("读取解释成果表-------数据格式： \n 井名，顶深 ，底深，解释厚度 ，有效厚度，孔隙度，渗透率，油饱和度，解释结论")
    filepath_interpretationData=u"testData\interpretation.txt"
    readFile_geo_interpretationData(filepath_interpretationData)
    
    


    
    

 

    
