# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock
import stockPatternRecognition
import configOS
import scipy.optimize as optimize
import math

def func(fData,a,b,c,d):
    return fData[0]*a+fData[1]*b+fData[2]*c + d

def historyPrint_optimize_curve_fit(cStock,countOfEle,kPeriod,params): 
    ##用模式识别的日期，寻找指数，然后找出比例 
    for indexDate in range(countOfEle-kPeriod,countOfEle-1):
        knum=3
        print("-"*72)
        print(cStock.dayStrList[indexDate-knum:indexDate])
        priceRiseRate3day=(cStock.dayRiseRateArray[indexDate-knum:indexDate]).mean()
        priceHigh3days=cStock.dayPriceHighestArray[indexDate-knum:indexDate].mean()
        priceClose3days=cStock.dayPriceClosedArray[indexDate-knum:indexDate].mean()
        priceLowFit=(cStock.dayPriceLowestArray[indexDate-knum:indexDate]*params[:3]).sum()+params[3]
        priceLow3days=cStock.dayPriceLowestArray[indexDate-knum:indexDate].mean()
        priceOpen3days=cStock.dayPriceOpenArray[indexDate-knum:indexDate].mean()
        priceWave3days=cStock.dayWaveRateArray[indexDate-knum:indexDate].mean()
        print("{}日涨幅平均{:.2f}，开盘均价{:.2f}，高均价{:.2f}，低均价{:.2f}，收盘均价{:.2f},平均波幅{:.2f}".format\
                (knum,priceRiseRate3day,priceOpen3days,priceHigh3days,priceLow3days,priceClose3days,priceWave3days))
        print("{}日最低价{:.2f}，最高价{:.2f}，最小波幅{:.2f}".format\
                (knum,cStock.dayPriceLowestArray[indexDate-knum:indexDate].min(),\
                cStock.dayPriceHighestArray[indexDate-knum:indexDate].max(),\
                cStock.dayWaveRateArray[indexDate-knum:indexDate].min() \
                )\
                )

        priceTbuy=priceLowFit*0.5+priceLow3days*0.5
        priceTsell=priceTbuy*1.025
        printTStop=priceTbuy*0.975
        print("最优化T-buy价{:.2f}，次日最低{},T-sell价{:.2f}，次日最高{},次日止损{:.2f},次日收盘{}".format(\
                priceTbuy,cStock.dayPriceLowestArray[indexDate+1],\
                priceTsell,cStock.dayPriceHighestArray[indexDate+1],\
                printTStop,cStock.dayPriceClosedArray[indexDate+1])\
                )
def patternRecCalTPrice(cStock,dayRadioLinkPriceLowArray):
    curMarket=Ccomfunc.getMarketStock(cStock.stockID)
    matchDateIndex=-1 ##识别日的指数
    stockPatternRecognition.patternRecByMarketAndStock(curMarket,cStock,matchDateIndex)
    listPatternRecBycStock=stockPatternRecognition.patternRecByRiseRate(cStock,300,3,matchDateIndex)
#    print listPatternRecBycStock
    findIndex=cStock.findIndexByDayStr("2012/05/21")
    scale= dayRadioLinkPriceLowArray[findIndex+1]
    print "匹配日此次预测低价{:.2f}".format(cStock.dayPriceLowestArray[-1]*(1+scale*0.01))

def outPutPriceRef(cStock):
    headWrited=[]
    wordWrited=[]
    for i in [3,5,8,13,21]:
        argsort=cStock.dayPriceLowestArray.argsort()
        headWrited.append("{}日低".format(i))
        headWrited.append("{}日高".format(i))
        wordWrited.append("{}".format(cStock.dayPriceLowestArray[-i:].min()))
        wordWrited.append("{}".format(cStock.dayPriceHighestArray[-i:].max()))
    print("\t".join(headWrited))
    print("\t".join(wordWrited))

def main(cStock):
    print ("一、 买卖的目的：1 建仓 2 T价差 3 控制仓位 4 止损")
    print ("二、 卖的条件：1 价差 2 时间差 价差没到，时间差到了，也要卖。")
    print ("三、 早盘买入要注意：1. 美股暴跌，10：30前不买。 2.高开10：30前不买")
    print ("四、 周五，指数在压力位附近，必须卖。")
    print ("-"*72)
    
    outPutPriceRef(cStock)
   
   
    ##买入点：用15分钟K线的支撑位买入T
    ##追高点：涨幅超过3个点绝对不能追高。
    ##卖出点：5日内高点，或者日内3个点。
    ##割肉点：三日破位或者大行情不好。

## 如果预测当日大盘好，用近期高点的97%作为买入点位。
## 预测大盘不好，用近期低点97%作为点位。

## 买入价一定要 超出买入预期，卖出价要降标准 

    countOfEle=len(cStock.dayStrList)
    dayRadioLinkPriceLowArray=np.zeros(countOfEle)
    for i in range(1,countOfEle):
        if cStock.dayPriceLowestArray[i-1]>0:
            dayRadioLinkPriceLowArray[i]=100*(cStock.dayPriceLowestArray[i]-cStock.dayPriceLowestArray[i-1])/cStock.dayPriceLowestArray[i-1]
#    print(dayRadioLinkPriceLowArray[-10:])
    
    
##----模式识别法买卖价计算模块
    ## 利用匹配日求取买入价
    ##用最近的一个匹配日的最低价的涨幅
    print("-"*72)
    print("\n模式识别法计算：")
    print("-"*72)
#    patternRecCalTPrice(cStock,dayRadioLinkPriceLowArray)
##----模式识别法买卖价计算模块
  
##----最优化方法买卖价计算模块
##仔细分析拟合算法
##利用3日的最低价做多项式拟合，周期选14。
    kPeriod=7 ##拟合区间
    indexDateFit=-3
    ##也可以用np.vstack((x,y,z))组合fData
    fDataLow=np.array([cStock.dayPriceLowestArray[indexDateFit-2-kPeriod:indexDateFit-2],\
            cStock.dayPriceLowestArray[indexDateFit-1-kPeriod:indexDateFit-1],\
            cStock.dayPriceLowestArray[indexDateFit-kPeriod:indexDateFit]])
    guess = (0.3,0.4,0.3,0)
    paramsLow, pcovLow = optimize.curve_fit(func, fDataLow,cStock.dayPriceLowestArray[-kPeriod:], guess)
    
    fDataHigh=np.array([cStock.dayPriceHighestArray[indexDateFit-2-kPeriod:indexDateFit-2],\
            cStock.dayPriceHighestArray[indexDateFit-1-kPeriod:indexDateFit-1],\
            cStock.dayPriceHighestArray[indexDateFit-kPeriod:indexDateFit]])
    paramsHigh, pcovHigh = optimize.curve_fit(func, fDataHigh,cStock.dayPriceHighestArray[-kPeriod:], guess)
#    print(paramsLow) ##最小二乘法计算参数
    
#    historyPrint_optimize_curve_fit(cStock,countOfEle,kPeriod,paramsLow)
    
    print("-"*72)
    print("最优化计算：")
    print("-"*72)
    priceTbuy=(cStock.dayPriceLowestArray[-3:]*paramsLow[:3]).sum()+paramsLow[3]
    priceTsell=priceTbuy*1.025
    printTStop=priceTbuy*0.975
    priceTfitHigh=(cStock.dayPriceHighestArray[-3:]*paramsHigh[:3]).sum()+paramsHigh[3]
    print("最优化T-buy价: {:.2f}，T-sell价: {:.2f}, T-FitHigh价: {:.2f}, T-stop价: {:.2f}".format(priceTbuy,priceTsell,priceTfitHigh,printTStop))
##----最优化方法买卖价

    print("-"*72)
##----5日最值法买卖价模块
    print("\n最值法计算：")
    print("-"*72)
    for period in [3,5,7]:
        indexHighPoint=Ccomfunc.rindex(cStock.dayPriceHighestFList,max(cStock.dayPriceHighestFList[countOfEle-period:]))
        indexLowPoint=Ccomfunc.rindex(cStock.dayPriceLowestFList,min(cStock.dayPriceLowestFList[countOfEle-period:]))
        priceHigh=cStock.dayPriceHighestFList[indexHighPoint]
        priceLow=cStock.dayPriceLowestFList[indexLowPoint]
        print("{}日最高点:{}，出现日期:{}, {}日最低点:{}，出现日期:{}".format( \
                period,priceHigh,cStock.dayStrList[indexHighPoint], \
                period,priceLow,cStock.dayStrList[indexLowPoint]))
        print("-"*72)
##----5日最值法买卖价模块

##----大盘的幅度差的买卖法
    print("-"*72)
    print("\n利用大盘调整的幅度差控制买卖点")
    print("-"*72)
##----模块

##----个股日内调整的幅度均值
    print("-"*72)
    print("\n个股日内调整的均值买卖")
    print("-"*72)
##----模块


    print("-"*72)
    for i in range(-3,0): ##循环指数起始比匹配指数少1
        weekDay=Ccomfunc.convertDateStr2Date(cStock.dayStrList[i]).isoweekday() 
        resultLine="{},星期{}\t收盘价:{}\t涨幅:{}\t量能环比:{}\t波动幅度:{}".format(\
                cStock.dayStrList[i],weekDay,cStock.dayPriceClosedArray[i],cStock.dayRiseRateFList[i],\
                cStock.dayRadioLinkOfTradeVolumeFList[i],cStock.dayWaveRateFList[i])
        print resultLine

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
    stocIDkList=["002152"]
    for stockID in stocIDkList:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
