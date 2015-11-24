# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock
import stockPatternRecognition

import scipy.optimize as optimize

def func(fData,a,b,c,d):
    return fData[0]*a+fData[1]*b+fData[2]*c + d

def main(curStock):
    
    marketID='999999'
    if not curStock.stockID.startswith('6'):
        marketID='399001'

    curMarket=Cstock.Stock(marketID)
   
    print ("做T价格计算，做t是宁可错过，不能做错的方案，一定要有价差才能买入。。")
    
    ##买入点：用15分钟K线的支撑位买入T
    ##卖出点：5日内高点，或者日内3个点。
    ##割肉点：三日破位或者大行情不好。

## 如果预测当日大盘好，用近期高点的97%作为买入点位。
## 预测大盘不好，用近期低点97%作为点位。

## 买入价一定要 超出买入预期，卖出价要降标准 

    indexMax=len(curStock.dayStrList)
    dayRadioLinkPriceLowArray=np.zeros(indexMax)
    for i in range(1,indexMax):
        if curStock.dayPriceLowestArray[i-1]>0:
            dayRadioLinkPriceLowArray[i]=100*(curStock.dayPriceLowestArray[i]-curStock.dayPriceLowestArray[i-1])/curStock.dayPriceLowestArray[i-1]
#    print(dayRadioLinkPriceLowArray[-10:])
    
    
    ## 利用匹配日求取买入价
    ##用最近的一个匹配日的最低价的涨幅
    matchDateIndex=-1 ##识别日的指数
    stockPatternRecognition.patternRecByMarketAndStock(curMarket,curStock,matchDateIndex)
    listPatternRecBycurStock=stockPatternRecognition.patternRecByRiseRate(curStock,300,3,matchDateIndex)
#    print listPatternRecBycurStock
    findIndex=curStock.findIndexByDayStr("2012/05/21")
    scale= dayRadioLinkPriceLowArray[findIndex+1]
#    print "匹配日此次预测低价{:.2f}".format(curStock.dayPriceLowestArray[-1]*(1+scale*0.01))
  

##仔细分析拟合算法
##利用3日的最低价做多项式拟合，周期选14。
    kPeriod=7 ##拟合区间
    indexDateFit=-3
    ##也可以用np.vstack((x,y,z))组合fData
    fData=np.array([curStock.dayPriceLowestArray[indexDateFit-2-kPeriod:indexDateFit-2],\
            curStock.dayPriceLowestArray[indexDateFit-1-kPeriod:indexDateFit-1],\
            curStock.dayPriceLowestArray[indexDateFit-kPeriod:indexDateFit]])
    guess = (0.3,0.4,0.3,0)
    params, pcov = optimize.curve_fit(func, fData,curStock.dayPriceLowestArray[-kPeriod:], guess)
    print(params)
    ##用模式识别的日期，寻找指数，然后找出比例 
    for indexDate in range(indexMax-kPeriod,indexMax-1):
        knum=3
        print("-"*72)
        print(curStock.dayStrList[indexDate-knum:indexDate])
        priceRiseRate3day=(curStock.dayRiseRateArray[indexDate-knum:indexDate]).mean()
        priceHigh3days=curStock.dayPriceHighestArray[indexDate-knum:indexDate].mean()
        priceClose3days=curStock.dayPriceClosedArray[indexDate-knum:indexDate].mean()
        priceLowFit=(curStock.dayPriceLowestArray[indexDate-knum:indexDate]*params[:3]).sum()+params[3]
        priceLow3days=curStock.dayPriceLowestArray[indexDate-knum:indexDate].mean()
        priceOpen3days=curStock.dayPriceOpenArray[indexDate-knum:indexDate].mean()
        priceWave3days=curStock.dayWaveRateArray[indexDate-knum:indexDate].mean()
        print("{}日涨幅平均{:.2f}，开盘均价{:.2f}，高均价{:.2f}，低均价{:.2f}，收盘均价{:.2f},平均波幅{:.2f}".format\
                (knum,priceRiseRate3day,priceOpen3days,priceHigh3days,priceLow3days,priceClose3days,priceWave3days))
        print("{}日最低价{:.2f}，最高价{:.2f}，最小波幅{:.2f}".format\
                (knum,curStock.dayPriceLowestArray[indexDate-knum:indexDate].min(),\
                curStock.dayPriceHighestArray[indexDate-knum:indexDate].max(),\
                curStock.dayWaveRateArray[indexDate-knum:indexDate].min() \
                )\
                )

        priceTbuy=priceLowFit*0.5+priceLow3days*0.5
        priceTsell=priceTbuy*1.025
        printTStop=priceTbuy*0.975
        print("3日T-buy价{:.2f}，次日最低{},T-sell价{:.2f}，次日最高{},次日止损{:.2f},次日收盘{}".format(\
                priceTbuy,curStock.dayPriceLowestArray[indexDate+1],\
                priceTsell,curStock.dayPriceHighestArray[indexDate+1],\
                printTStop,curStock.dayPriceClosedArray[indexDate+1])\
                )

    print("$"*72)
    priceTbuy=(curStock.dayPriceLowestArray[-3:]*params[:3]).sum()+params[3]
    priceTsell=priceTbuy*1.025
    printTStop=priceTbuy*0.975
    print("{}收盘价{},{}日最低价{:.2f}，最高价{:.2f}，最小波幅{:.2f}".format\
                ( curStock.dayStrList[-1],curStock.dayPriceClosedArray[-1],\
                  knum,curStock.dayPriceLowestArray[-3:].min(), curStock.dayPriceHighestArray[-3:].max(),\
                curStock.dayWaveRateArray[-3:].min() \
                )\
        )
    print("3日T-buy价{:.2f}，T-sell价{:.2f},T-stop价{:.2f}".format(priceTbuy,priceTsell,printTStop))
    
    for period in [3,5,10]:
        indexHighPoint=curStock.dayPriceHighestFList.index(max(curStock.dayPriceHighestFList[-period:]))
        indexLowPoint=curStock.dayPriceLowestFList.index(min(curStock.dayPriceLowestFList[-period:]))
        priceHigh=curStock.dayPriceHighestFList[indexHighPoint]
        priceLow=curStock.dayPriceLowestFList[indexLowPoint]
        print("{}日最高点{}，出现日期{},{}日最低点{}，出现日期{}".format( \
                period,priceHigh,curStock.dayStrList[indexHighPoint], \
                period,priceLow,curStock.dayStrList[indexLowPoint]))
        print("%95buy: {:.2f},%93buy: {:.2f}".format(priceHigh*0.95,priceHigh*0.93))
    print("$"*72)

    for i in range(-3,0): ##循环指数起始比匹配指数少1
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        resultLine="{},星期{}\t收盘价:{}\t涨幅:{}\t量能环比:{}\t波动幅度:{}".format(\
                curStock.dayStrList[i],weekDay,curStock.dayPriceClosedArray[i],curStock.dayRiseRateFList[i],\
                curStock.dayRadioLinkOfTradeVolumeFList[i],curStock.dayWaveRateFList[i])
        print resultLine
##放量上涨
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]>1 and curStock.dayRiseRateArray[-1]>0:
        print("放量上涨。")
##缩量上涨
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]>0:
        print("缩量上涨。")
##放量下跌
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]<0:
        print("放量下跌。")
##缩量下跌
    if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]<0:
        print("缩量下跌。")
    
    marketMood=1
    if marketMood<=0.5:
        print("3日T均价{:.2f}".format(priceLow3days*0.5+priceClose3days*0.5))



    ## 美股-1.5以上，当日上午不买做T，可以适度的上午减仓做T。 
    ## 设计做T的价格，用15分钟K线的支撑或者其它点位。
    ## 大盘涨价少 跌家多 不做短线。 
    


    ##做T的价格如果低了2个点 坚决出。

    ## 如果当天预测行情不好，绝对不加仓买，宁可不动 
    ## 做T应该根据开盘价，大盘与个股的走势关系联动。高抛低吸。注意保持仓位。但是大盘必须是震荡市，不能是单边市
    ## 单边市和震荡市的判断，需要结合大盘和个股作分析。
    ## 如何T飞了 或者仓位不够的话，可以尾盘2：45再买回来！宁可不赚钱，不能赔钱。
    ## 弱势别想着暴涨，卖了就涨飞了？那种可能性也不是那么大的。一年也不会发生几回。而且平摊了仓位风险。亏不了多少。

    
    print ("严格的执行止损方案。")

if __name__=="__main__":
    
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    for stockID in ["600178","002001"]:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
