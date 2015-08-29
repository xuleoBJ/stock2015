# -*- coding: utf-8 -*-
import os
import numpy as np
import shutil
import time
import datetime
import Cstock
import Ccomfunc

##计算按周期计算涨停幅度

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    Ccomfunc.printInfor()
    
    startClock=time.clock() ##记录程序开始计算时间

    ##读取股票代码，存储在curStock里
    stockID="002673"
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
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"个交易日内统计：\n涨幅区间个数:\t"
        print(headLine)
        fileWrited.write(headLine)
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i<=x<i+1,curStock.riseRateFList[-days:]))
            if i==10:
                _line="涨停版\t"+str(_num)
            else :
                _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')
    ##计算周期内涨的频率并绘直方图
    ##分析高开低走，低开高走，高开高走，低开低走的个数
    ##计算每天振幅的幅度分布并绘图
    ##涨停或者跌停出现的个数
    ##高开的天数，低开的天数
    ##设置分析周期
    ##成交量变动分析
#    print ("正在分析成交量变动：")
#    for i in range(-20,-1):
#        print curStock.dateStrList[i],curStock.riseOfTradeVolumeFList[i],curStock.riseOfTurnOverFList[i]
#    for i in range(-iDaysPeriodUser,-1):
#        ##这里变更条件找历史图行，又一周的行情分析
#        if curStock.riseRateFList[i-2]<=-3 and curStock.riseRateFList[i]>=3 and curStock.priceClosedFList[i-2]>curStock.priceClosedFList[i-1]:
#            if curStock.waveRateFList[i]>=3: ##振幅
#               if curStock.tradeVolumeFList[i-2]>curStock.tradeVolumeFList[i-1]>curStock.tradeVolumeFList[i]: ## 成交量
#                print(curStock.dateStrList[i])
#                fileWrited.write(curStock.dateStrList[i]+'\n')
#                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


