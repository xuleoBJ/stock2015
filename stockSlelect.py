# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc

##计算按周期计算涨停幅度

lineWrited=[]

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
   

    stockIDList=[]
    
    if len(stockIDList)==0:
        fileNames=os.listdir(Ccomfunc.dirData)
        for fileItem in fileNames:
            ##根据字头选择文件 上证6 深圳 0 板块指8 创业板 3
            if os.path.basename(fileItem).startswith("8"):
                stockIDList.append(os.path.splitext(fileItem)[0])
    
   
    print ("正在根据条件筛选股票：")
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法
    lineWritedList=[]
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        sMonth="201212"
        for i in range(len(curStock.monthStrList)):
            if curStock.monthStrList[i].endswith(sMonth):
                lineWritedList.append(curStock.stockID+"\t"+curStock.stockName+"\t"+sMonth+"\t"+str(curStock.monthRiseRateFList[i]))
    ##输出文件名
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


