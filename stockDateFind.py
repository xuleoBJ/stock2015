## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock


##计算按周期计算涨停幅度

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("控制风险，保持耐心，态度认真。")
    print ("下跌过程永远不买票！企稳后再买卖！最好是尾盘15分钟买卖！要么就挂相对的低价单钓鱼。")
    print ("在历史K线中寻找有类似特征信息的日期，因为历史是重复的，错误也是循环的。")
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
    iDaysPeriodUser=len(curStock.dateStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print ("正在查找历史K线日期：")
    for i in range(-iDaysPeriodUser+2,-1):
        ##这里变更条件找历史图行，又一周的行情分析
        if curStock.riseRateFList[i-2]>=2.2 and curStock.riseRateFList[i-1]>=4.5 and -0.5<=curStock.riseRateFList[i]<=0.5:
 ##    if curStock.riseRateFList[i-2]<= curStock.riseRateFList[i-1]<=curStock.riseRateFList[i]<0 and curStock.priceCloseingFList[i-2]>curStock.priceCloseingFList[i-1]>curStock.priceCloseingFList[i]:
 ##       if  curStock.riseRateFList[i-3]>=2 and curStock.riseRateFList[i]<=-2:  ##
 ##           if curStock.waveRateFList[i]>=3: ##振幅
 ##             if curStock.riseOfTradeVolumeFList[i]<-20:
                print(curStock.dateStrList[i])
                fileWrited.write(curStock.dateStrList[i]+'\n')
                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


