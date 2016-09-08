# -*- coding: utf-8 -*-
import os
import Ccomfunc

##两种方法获得stockIDList，selectScale=1 从文本文件stockIDList.txt 读取 =2，海选
def makeStockList(selectScale=2):
    stockIDList=["999999","399001"]
    stockIDListNot=[]
    with open('stockIDListNot.txt') as fOpen:
        for line in fOpen:
            inner_list = [elt.strip() for elt in line.split(' ')]
            stockIDListNot.append(inner_list[0])
    
    
    ## 根据文件名的第一个字符区分股票类别  上证6 深圳 0 板块指8 创业板 3
    stockIDType=["8","3","6","0"]
    if selectScale == 1: ##限选
        with open('stockIDList.txt') as fOpen:
            for line in fOpen:
                inner_list = [elt.strip() for elt in line.split(' ')]
                stockIDList.append(inner_list[0])
    if selectScale == 2 :  ##海选
        fileNames=os.listdir(Ccomfunc.src)
        for fileItem in fileNames:
            curFileName = os.path.basename(fileItem) 
            if curFileName not in stockIDListNot and curFileName[0] in stockIDType: ## 根据文件名的第一个字符区分股票类别 
                stockIDList.append(os.path.splitext(fileItem)[0])
    return stockIDList

##输入代码IDtext路径，makeIDList,第一列为ID代码
def makeStockListFromIDtxt(filePathIDtxt):
    stockIDList=[]
    with open(filePathIDtxt) as fOpen:
        for line in fOpen:
            inner_list = [elt.strip() for elt in line.split(' ')]
            stockIDList.append(inner_list[0])
    return stockIDList
