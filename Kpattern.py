# -*- coding: utf-8 -*-
import os,math
import Cstock
#print "hello,world"
### engulfing pattern 确定趋势中的大阴包大阳，算法是第二天收盘价小于第一天的开盘价并且两根长柱子
#if curStock.dayRiseRateCloseFList[i-1]>=2 and curStock.dayRiseRateCloseFList[i]<=-2 and curStock.priceCloseingFList[i]<curStock.dayPriceOpenFList[i-1] and  curStock.priceCloseingFList[i-1]<curStock.dayPriceOpenFList[i]:
#
### price rate	
#if 0<curStock.dayRiseRateCloseFList[i-2]<=1 and -0.5<=curStock.dayRiseRateCloseFList[i-1]<=0.5 and 2<=curStock.dayRiseRateCloseFList[i]:
#
### 连跌3天，但是每天的跌幅变小
#if curStock.dayRiseRateCloseFList[i-2]<= curStock.dayRiseRateCloseFList[i-1]<=curStock.dayRiseRateCloseFList[i]<0 and curStock.priceCloseingFList[i-2]>curStock.priceCloseingFList[i-1]>curStock.priceCloseingFList[i]:
#
# hammer pattern criteria P29
#1 the real body is at the upper end of the trading range.The color of the real body is not important
# 2 a long lower shadow should be twice the height of the real body
# 3 it should  have no a very short, upper shadow
def patternHammer(openPrice,closePrice,highPrice,lowPrice):
    if abs(highPrice-lowPrice)>=3 and abs(highPrice-lowPrice)/abs(closePrice-openPrice)>=3 and (abs(highPrice-closePrice)<=0.05 or abs(highPrice-openPrice)<=0.05):
        return True
    else:
        return False


# engulfing pattern criteria P39
# 1 the market has to be in a clear definable uptrend or downtrend, even the trend is short term
# 2 two candle sticks compise the engulfing pattern. The second real body must engulf the prior body(it need not engulf the shadows)
# 3 the second real body of the engulfing pattern should be the opposite color of the first real body

def patternEngulfBull(curstock,index):
    if curstock.dayRiseRateCloseFList[index-1]<=-2 and curstock.dayRiseRateCloseFList[index]>=3 and curstock.daysPriceOpenFList[index]>= curstock.daysPriceClosedFList[index-1]:
        return True
    else:
        return False

def patternEngulfBear(curstock,index):
    if 0.5<=curstock.dayRiseRateCloseFList[index-1]<=1 and curstock.dayRiseRateCloseFList[index]<=-3 and curstock.daysPriceOpenFList[index] >= curstock.daysPriceClosedFList[index-1]:
        return True
    else:
        return False

#Dark-cloud cover
def patternDarkCloudCover(curstock,index):
    if curstock.dayRiseRateCloseFList[index-1]>=3 and curstock.dayRiseRateCloseFList[index]<=-3 and curstock.daysPriceClosedFList[index]< curstock.daysPriceClosedFList[index-1]:
        return True
    else:
        return False

#GraveStone
def patternDarkCloudCover(curstock,index):
    if curstock.dayWaveRateFList[index]>=3 and curstock.daysPriceClosedFList[index]== curstock.daysPriceOpenFList[index]:
        return True
    else:
        return False

#DOJI
def patternDOJIBull(curstock,index):
    if curstock.dayRiseRateCloseFList[index-1]<=-2 and curstock.daysPriceOpenFList[index] <= curstock.daysPriceClosedFList[index-1] and curstock.daysPriceOpenFList[index]== curstock.daysPriceClosedFList[index]:
        return True
    else:
        return False

def patternDOJIBear(curstock,index):
    if curstock.dayRiseRateCloseFList[index-1]>=2 and curstock.daysPriceOpenFList[index] >= curstock.daysPriceClosedFList[index-1] and curstock.daysPriceOpenFList[index]== curstock.daysPriceClosedFList[index]:
        return True
    else:
        return False

#Evening star
def patternEveningStar(curstock,index):
    if patternDOJIBear(curstock,index-1)==True and curstock.dayRiseRateCloseFList[index]<=2:
        return True
    else:
        return False

#Piercing Pattern
def patternPiercingPattern(curstock,index):
    if curstock.dayRiseRateCloseFList[index-1]<=-2 and curstock.daysPriceOpenFList[index] <= curstock.daysPriceClosedFList[index-1] and curstock.daysPriceClosedFList[index]>0.5*(curstock.daysPriceClosedFList[index-1]+ curstock.daysPriceOpenFList[index-1]):
        return True
    else:
        return False
