#-*- coding:utf-8 -*-
import os
import xlrd
import sys

##无效值
VALUE_INVALID=-999
##错误信息文件path
erInforFilePath=u"data\errInfor.txt"
modelDataBaseFilePath=u"data\modelDataBase.txt"
##存储井头信息
wellHeadInfor_list=[]  ##list[list], 每个list 包括wellname，x（float），y（float），KB

##存储小层名信息
layerName_strList=[] ##层名strlist

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


def effInforWrited(errInforLine=""):
    open(erInforFilePath,'w').write(errInforLine)

def readFile_geo_wellhead(filepath_wellHead):
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
    print("完成井头数据读取。")
    
def readFile_geo_wellDeviation():

    print("完成井斜数据读取。")

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

def readFile_geo_layerName(filepath_layerName):
    fileOpened_layerName=open(filepath_layerName,'r')
    lineIndex=0
    for line in fileOpened_layerName.readlines():
         lineIndex= lineIndex+1
         if line!="" and lineIndex>1:
            splitLine=line.split()
            layerName_strList.append(splitLine[0])
    print("完成地层名读取。")


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

def completeLayerData():
    ##根据井头信息和井斜数据，校正顶底深，填海拔深度表
    ## 根据测井解释成果表，完善小层数据表的孔渗饱加权数据，
    ##文件写入文本文件modelDataBaseFilePath
    print("根据解释成果表，计算welltop数据")
    lineHead="jh\txcm\tX\tY\ttopDepth(ele)\tbottomDepth(ele)\tlayerHou\tyxhd\tPor\tPer\tSo\n"
    fileOpenedModelDataBase=open(modelDataBaseFilePath,'w')
    fileOpenedModelDataBase.write(lineHead)
    for i in range(len(wellName_wellTop_strList)):
        linetemp=[]
        for wellHeadItem in wellHeadInfor_list:
            if wellName_wellTop_strList[i]==wellHeadItem[0]:
                X_wellTop_floatList[i]=wellHeadItem[1]
                Y_wellTop_floatList[i]=wellHeadItem[2]
                topElevation_wellTop_floatList[i]=round(wellHeadItem[3]-topDepth_wellTop_floatList[i],2)
                bottomElevation_wellTop_floatList[i]=round(wellHeadItem[3]-bottomDepth_wellTop_floatList[i],2)
                layerThickness_wellTop_floatList[i]=round(bottomDepth_wellTop_floatList[i]-topDepth_wellTop_floatList[i],2)
                sandThickness_wellTop_floatList[i]=0
                por_wellTop_floatList[i]=0
                per_wellTop_floatList[i]=0
                so_wellTop_floatList[i]=0
        for j in range(len(wellName_interpretation_strList)):
            if topDepth_wellTop_floatList[i]<=topDepth_interpretation_floatList[j] and  \
                bottomDepth_interpretation_floatList[j]<=bottomDepth_wellTop_floatList[i]:
                sandThickness_wellTop_floatList[i]=round(sandThickness_wellTop_floatList[i]+sandThickness_interpretation_floatList[j],2)
                por_wellTop_floatList[i]=por_wellTop_floatList[i]+por_interpretation_floatList[j]*sandThickness_interpretation_floatList[j]
                per_wellTop_floatList[i]=per_wellTop_floatList[i]+per_interpretation_floatList[j]*sandThickness_interpretation_floatList[j]
                so_wellTop_floatList[i]=so_wellTop_floatList[i]+so_interpretation_floatList[j]*sandThickness_interpretation_floatList[j]

        if sandThickness_wellTop_floatList[i]>0:
            por_wellTop_floatList[i]=round(por_wellTop_floatList[i]/sandThickness_wellTop_floatList[i],2)
            per_wellTop_floatList[i]=round(per_wellTop_floatList[i]/sandThickness_wellTop_floatList[i],2)
            so_wellTop_floatList[i]=round(so_wellTop_floatList[i]/sandThickness_wellTop_floatList[i],2)
        else:
            por_wellTop_floatList[i]=VALUE_INVALID
            per_wellTop_floatList[i]=VALUE_INVALID
            so_wellTop_floatList[i]=VALUE_INVALID
            
        linetemp.append(wellName_wellTop_strList[i])
        linetemp.append(layerName_wellTop_strList[i])
        linetemp.append(X_wellTop_floatList[i])
        linetemp.append(Y_wellTop_floatList[i])
        linetemp.append(topElevation_wellTop_floatList[i])
        linetemp.append(bottomElevation_wellTop_floatList[i])
        linetemp.append(layerThickness_wellTop_floatList[i])
        linetemp.append(sandThickness_wellTop_floatList[i])
        linetemp.append(por_wellTop_floatList[i])
        linetemp.append(per_wellTop_floatList[i])
        linetemp.append(so_wellTop_floatList[i])
        fileOpenedModelDataBase.write( '\t'.join(map(str,linetemp))+'\n')

    print(u"welltop数据文件生成。")
    fileOpenedModelDataBase.close()



def generateModelingLayerData(layerSelected):
    filewritedGenerateLayerData=open(u'layer\\'+layerSelected+'layer.txt','w')
    lineHead="jh\txcm\tX\tY\ttopDepth\tbottomDepth\tshaHou\tyxhd\tPor\tPer\tSo\n"
    filewritedGenerateLayerData.write(lineHead)
    for i in range(len(wellName_wellTop_strList)):
        if layerName_wellTop_strList[i]==layerSelected:
            wellItem=[]
            wellItem.append(layerSelected)
            wellItem.append(wellName_wellTop_strList[i])
            wellItem.append(X_wellTop_floatList[i])
            wellItem.append(Y_wellTop_floatList[i])
            wellItem.append(topElevation_wellTop_floatList[i])
            wellItem.append(bottomElevation_wellTop_floatList[i])
            wellItem.append(layerThickness_wellTop_floatList[i])
            wellItem.append(sandThickness_wellTop_floatList[i])
            wellItem.append(por_wellTop_floatList[i])
            wellItem.append(per_wellTop_floatList[i])
            wellItem.append(so_wellTop_floatList[i])
            print(wellItem)
            filewritedGenerateLayerData.write( '\t'.join(map(str,wellItem))+'\n')
    filewritedGenerateLayerData.close()
    print(u"建模基础文件生成。")


    
if __name__=="__main__":
    
    print("读取井头数据，请注意X,Y的顺序-------数据格式： \n井名，X坐标，Y坐标，补心海拔  ")
    filepath_wellHead=u"data\wellHead.txt"
    readFile_geo_wellhead(filepath_wellHead)


    print("读取井斜轨迹-------数据格式： \n井名  ，X坐标(东西)，Y坐标(南北)，垂深/海拔	斜深  ")
    readFile_geo_wellDeviation()

    print("读取层位数据，请注意按照从上到下的顺序-------")
    filepath_layerName=u"data\layerName.txt"
    readFile_geo_layerName(filepath_layerName)

    print("读取解释成果表-------数据格式： \n 井名，顶深 ，底深，解释厚度 ，有效厚度，孔隙度，渗透率，油饱和度，解释结论")
    filepath_interpretationData=u"data\interpretation.txt"
    readFile_geo_interpretationData(filepath_interpretationData)

    print("读取分层数据-------数据格式： \n 井名，小层名，小层顶深 ，小层底深")
    filepath_wellTop=u"data\wellTop.txt"
    readFile_geo_wellTop(filepath_wellTop)
    
    print("正在对小层数据表进行数据校正调整：")
    
    completeLayerData()


    for layerItem in layerName_strList:
        generateModelingLayerData(layerItem)

    print("正在进行建模数据质量检测：\n")

    print("正在计算小层非均质性：\n")

    print("正在计算单井模型：\n")
    
    print("正在计算建模基础数据表，数据格式：\n wellName,layerName,X,Y ,海拔顶深，层厚，砂厚，pore，per，So")

    print("读取边界数据：")

    print("读取X,Y方向步长数据及与x方向交角：")
    
    print("print井信息——————")
    for i in range(len(wellHeadInfor_list)):
        print(wellHeadInfor_list[i])
    
##    print(wellName_interpretation_strList,)
##    print(topDepth_interpretation_floatList)
##    print(bottomDepth_interpretation_floatList)

    
    

 

    
