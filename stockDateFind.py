## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock


##计算按周期计算涨停幅度

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析价差和涨幅")
    
    zhenfuFList=[] ## 波动幅度
    zhangdiefuFList=[]  ##涨跌幅
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i]-priceOpeningFList[i])/priceCloseingFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceCloseingFList[i-1]
        if priceDelta1>=0.05:
            zhenfuFList.append(i)
        if abs(priceDelta2)>=0.05:
            zhangdiefuFList.append(i)
    strDate=""
    for item in zhenfuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("振幅超过5%天数:\t"+str(len(zhenfuFList))+"\t起始日期是："+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("涨跌幅超过5%:\t"+str(len(zhangdiefuFList))+"\t起始日期是："+strDate)

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print ("分析大的趋势和振幅，波峰和波谷。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
   
    ##读取上证指数数据
    ##shStock=Cstock.StockSH()
    

    ##读取股票代码，存储在curStock里
    stockID="999999"
    curStock=Cstock.Stock(stockID)
    
    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

    ##设置分析周期
    iDaysPeriodUser=5000
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser-1]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print ("正在进行时空分析：")
    for i in range(-iDaysPeriodUser,-1):
        ##这里变更条件找历史图行，又一周的行情分析
        if  curStock.riseRateFList[i-3]>=2 and curStock.riseRateFList[i]<=-2:  ##
            if curStock.waveRateFList[i]>=3: ##振幅
 ##              if (curStock.tradeVolumeFList[i]-curStock.tradeVolumeFList[i-1])/curStock.tradeVolumeFList[i-1]>=0.1: ## 成交量
                print curStock.dateStrList[i]
                fileWrited.write(curStock.dateStrList[i]+'\n')
                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


