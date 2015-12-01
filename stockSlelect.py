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
            if os.path.basename(fileItem).startswith("8") or os.path.basename(fileItem).startswith("9") :
                stockIDList.append(os.path.splitext(fileItem)[0])
    
   
    print ("正在根据条件筛选股票：")
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法
    lineWritedList=[]
    monthStrList=["201112","201212","201312","201412"]
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        sList=[]
        sList.append(curStock.stockID)
        sList.append(curStock.stockName)
        for sMonth in monthStrList:
            sList.append(sMonth)
            _riseRateMonth="-999"
            for i in range(len(curStock.monthStrList)):
                if curStock.monthStrList[i].endswith(sMonth):
                    _riseRateMonth=str(curStock.monthRiseRateFList[i])
            sList.append(_riseRateMonth)
        lineWritedList.append("\t".join(sList))
    ##输出文件名
    
    ##分析寻找涨幅最大板块中，当月涨幅最大的个数
    
    ##分析寻找涨幅最大板块中，连续3-5个交易日涨幅最大的个股
    
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


