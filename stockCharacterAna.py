# -*- coding: utf-8 -*-  
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  

lineWrited=[]

##根据涨幅，第二天趋势分析
##fList是需要分析的数据list，比如涨幅，或者高开数据，flow是数据区间的下限值，fHigh是数据区间的上限值
def countTrendByRiseRate(cStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(cStock.dayRiseRateFList)-1):
        if fLow<=cStock.dayRiseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("满足条件个数：{},>0的个数{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

##根据第一天的走势，第二天趋势分析
##fList是需要分析的数据list，比如涨幅，或者高开数据，flow是数据区间的下限值，fHigh是数据区间的上限值
def countTrendByOpenCloseRate(cStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(cStock.dayOpenCloseRateFList)-1):
        if fLow<=cStock.dayRiseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("满足条件个数：{},>0的个数{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

def trend(cStock):
    print ("过去3年同期20个交易日走势：")
    today=datetime.date.today()
    for i in [1,2,3]:
        todayLastYear=today-datetime.timedelta(days=365*i) ##不准确但是可行
        print "{}年同期涨幅：".format(todayLastYear.year)
        for item in cStock.dateList:
            if todayLastYear-datetime.timedelta(days=1)<=item<=todayLastYear+datetime.timedelta(days=10):
                _index=cStock.dateList.index(item)
                print cStock.dayStrList[_index],cStock.dayRiseRateFList[_index]


def compareStockAndMarket(cStock,strDateStart,strDateEnd):
    cMarketStock=Ccomfunc.getMarketStock(cStock.stockID) 
    dataDraw=[]
    indexOfStart=Ccomfunc.getIndexByStrdate(cStock,strDateStart)
    indexOfEnd=Ccomfunc.getIndexByStrdate(cStock,strDateEnd)
    ##区间涨幅
    rise= 100*(cStock.dayPriceClosedFList[indexOfEnd]-cStock.dayPriceClosedFList[indexOfStart-1])/cStock.dayPriceClosedFList[indexOfStart-1]
    dataDraw.append(rise)
    print "涨幅：{:.2f}".format(rise) 
    indexMax=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmax()
    indexMin=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmin()
    print "区间低点出现日期：{}，高点日期：{}".format(cStock.dayStrList[indexMin],cStock.dayStrList[indexMax])
    
    dateTick=range(iYearStart,iYearEnd)
    
    ind =np.arange(len(dateTick))    # the x locations for the groups
    width=0.35
    
    p1 = plt.bar(ind, dataDraw, width, color='r')
    plt.ylabel(u'riseRate')
    plt.title(cStock.stockID)
    ax=plt.gca()
    ymajorLocator = MultipleLocator(1) #将y轴主刻度标签设置为0.5的倍数
    ax.yaxis.set_major_locator(ymajorLocator)    
    plt.xticks(ind + width/2., dateTick)
    plt.show()

def statisticsRiselrate(cStock,iYearStart,iYearEnd,sMDStart,sMDEnd):## sMDStart="08/08"
     ##过去n年同期某个时间段的涨幅，最高点出现的时间，最低点出现的时间
    dataDraw=[]
    print("##统计分析最近不同交易周期内，不同涨幅的个数分布频率")
    for year in range(iYearStart,iYearEnd):
        headLine=str(year)+"年"+sMDStart+"-"+sMDEnd+"高点和低点出现统计分析："
        print(headLine)
        dateStrStart=str(year)+"/"+sMDStart
        indexOfStart=Ccomfunc.getIndexByStrdate(cStock,dateStrStart)
        dateStrEnd=str(year)+"/"+sMDEnd
        indexOfEnd=Ccomfunc.getIndexByStrdate(cStock,dateStrEnd)
        ##区间涨幅
        rise= 100*(cStock.dayPriceClosedFList[indexOfEnd]-cStock.dayPriceClosedFList[indexOfStart-1])/cStock.dayPriceClosedFList[indexOfStart-1]
        dataDraw.append(rise)
        print "涨幅：{:.2f}".format(rise) 
        indexMax=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmax()
        indexMin=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmin()
        print "区间低点出现日期：{}，高点日期：{}".format(cStock.dayStrList[indexMin],cStock.dayStrList[indexMax])
    
    dateTick=range(iYearStart,iYearEnd)
    
    ind =np.arange(len(dateTick))    # the x locations for the groups
    width=0.35
    
    p1 = plt.bar(ind, dataDraw, width, color='r')
    plt.ylabel(u'riseRate')
    plt.title(cStock.stockID)
    ax=plt.gca()
    ymajorLocator = MultipleLocator(1) #将y轴主刻度标签设置为0.5的倍数
    ax.yaxis.set_major_locator(ymajorLocator)    
    plt.xticks(ind + width/2., dateTick)
    plt.show()

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间

    stockID="002001"
    ##读取股票代码，存储在curStock里
    curStock=Cstock.Stock(stockID)
    curStock.list2array()
    curMarketStock=Ccomfunc.getMarketStock(stockID) 
    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')
    
    ##过去n年同期某个时间段的涨幅，最高点出现的时间，最低点出现的时间
    print("##统计分析最近不同交易周期内，不同涨幅的个数分布频率")
    iYearStart=2010
    iYearEnd=2015
    strDateStart="12/01"
    strDateEnd="12/31"
    dataDraw=statisticsRiselrate(curStock,iYearStart,iYearEnd,strDateStart,strDateEnd)
  
#    for year in range(2000,2015):
#        headLine=str(year)+"年12月高点和低点出现统计分析："
#        print(headLine)
#        dateStrStart=str(year)+"/12/01"
#        indexOfStart=Ccomfunc.getIndexByStrdate(curStock,dateStrStart)
#        dateStrEnd=str(year)+"/12/31"
#        indexOfEnd=Ccomfunc.getIndexByStrdate(curStock,dateStrEnd)
#        ##区间涨幅
#        rise= 100*(curStock.dayPriceClosedFList[indexOfEnd]-curStock.dayPriceClosedFList[indexOfStart-1])/curStock.dayPriceClosedFList[indexOfStart-1]
#        dataDraw.append(rise)
#        print "涨幅：{:.2f}".format(rise) 
#        indexMax=indexOfStart+curStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmax()
#        indexMin=indexOfStart+curStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmin()
#        print "区间低点出现日期：{}，高点日期：{}".format(curStock.dayStrList[indexMin],curStock.dayStrList[indexMax])
#        fileWrited.write(headLine+"\n")

  
    
    ##设置分析周期
    iDaysPeriodUser=len(curStock.dayStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]
   
    ##增加时间点统计，可以有趋势的效果

    ##统计分析最近不同交易周期内，不同涨幅的个数分布频率
    print("##统计分析最近不同交易周期内，不同涨幅的个数分布频率")
    for dayPeriod in [300,150,90,60,30,20,10,5]:
        headLine=str(dayPeriod)+"个交易日内统计：\n涨幅区间个数:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayRiseRateFList[-dayPeriod:]))
            if i==10:
                _line="涨停版\t"+str(_num)
            else :
                _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')
    
    ##分析不同交易周期内，统计不同波动幅度的个数频率
    print("##分析不同交易周期内，统计不同波动幅度的个数频率")
    for dayPeriod in [300,150,90,60,30,20,10,5]:
        headLine=str(dayPeriod)+"个交易日内统计：\n振幅区间个数:\t"
        fileWrited.write(headLine+"\n")
        for i in range(0,21):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayWaveRateFList[-dayPeriod:]))
            _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')
    
    ##分析不同交易周期内，统计开盘高开，低开的频率
    print("##分析不同交易周期内，统计开盘高开，低开的频率")
    for dayPeriod in [30,20,10,5]:
        headLine=str(dayPeriod)+"个交易日内统计：\n开盘的涨幅频率分布:\t"
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayOpenRateFList[-dayPeriod:]))
            _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')
    
    print("##分析不同交易周期内，统计最低值与开盘值频率分布")
    for dayPeriod in [300,150,90,60,30,20,10,5]:
        ##分析开盘价与最低价 差额相对于昨日价格的百分比分布
        ##如果开盘价就是最低价，差额就是0，如果开盘价比最低价差额不大，代表市场比较强
        ##如果开盘价与最低价差额比较大，代表空方力量比较大
        headLine=str(dayPeriod)+"个交易日内统计：\n分析开盘价与最低价 差额相对于昨日价格的百分比频率分布:\t \
        ##如果开盘价就是最低价，差额就是0，如果开盘价比最低价差额不大，代表市场比较强  \
        ##如果开盘价与最低价差额比较大，代表空方力量比较大 "
        fileWrited.write(headLine+"\n")
        for i in range(-20,1):
            _line=""
            _num=len(filter(lambda x:i==int(x),map(lambda x,y,z:100*(x-y)/z, \
                    curStock.dayPriceLowestFList[-dayPeriod:],curStock.dayPriceOpenFList[-dayPeriod:],curStock.dayPriceClosedFList[-dayPeriod-1:-1])))
            if i==0:
                _line="开盘价就是最低价\t"+str(_num)
            else :
                _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')

    ##分析不同交易周期内,高开低走，第二天的涨跌
    for i in range(-10,11):
        print("当日走势{}%-{}%，次日涨幅分布：".format(i,i+1))
        countTrendByOpenCloseRate(curStock,curStock.dayRiseRateFList,i-0.1,i+0.1)
  
    ##统计分析大盘跌4个点的交易日的走势和次日走势。
    
    ##统计分析 近期大盘开盘点位和最低点的差额,这个只能近期有效，长期无效
    ##最近10个交易日的浮动是对做t最好的参考资料。而不能凭感觉说 低了，或者高了！！！！
    ##分析高开低走，低开高走，高开高走，低开低走的个数
    ##高开的天数，低开的天数
    
    ##成交量变动分析
#    print ("正在分析成交量变动：")
#    for i in range(-20,-1):
#        print curStock.dayStrList[i],curStock.dayRiseOfTradeVolumeFList[i],curStock.dayRiseOfTurnOverFList[i]
#    for i in range(-iDaysPeriodUser,-1):
#        ##这里变更条件找历史图行，又一周的行情分析
#        if curStock.dayRiseRateFList[i-2]<=-3 and curStock.dayRiseRateFList[i]>=3 and curStock.dayPriceClosedFList[i-2]>curStock.dayPriceClosedFList[i-1]:
#            if curStock.dayWaveRateFList[i]>=3: ##振幅
#               if curStock.dayTradeVolumeFList[i-2]>curStock.dayTradeVolumeFList[i-1]>curStock.dayTradeVolumeFList[i]: ## 成交量
#                print(curStock.dayStrList[i])
#                fileWrited.write(curStock.dayStrList[i]+'\n')
#                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


