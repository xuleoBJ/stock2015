# -*- coding: UTF-8 -*-
import datetime
import lxml.etree as etree
import lxml.html
import ConfigParser
import time,sched,os,urllib2,re,string
import ctypes
from Cstock import Stock
import numpy as np


def mymain():
    curStock=Stock('399001')
    shStock=Stock('999999')
    print (u"量能对比分析最后5个交易日量能对比：")
    print shStock.stockID,shStock.stockName,shStock.dayStrList[-5:],shStock.dayRadioLinkOfTradeVolumeFList[-5:]
    print curStock.stockID,curStock.stockName,curStock.dayStrList[-5:],curStock.dayRadioLinkOfTradeVolumeFList[-5:]


##period 是量能情绪控制周期
def moodIndex(curStock,period):
    print (u"{}日情绪指数分析".format(period))
#   计算最近period个交易日内的量能排序,通过量能分析市场情绪 
    sortIndexList=curStock.dayTradeVolumeArray[-period:].argsort()
#    print sortIndexList ## 输出指数，注意是 [-period:]中的位置
    
    ##正情绪指数选取的参数天数
    numOfmoodDay=5
    if period<20:
        numOfmoodDay=3
    print (u"交易量最大的交易日：")
    
    tradeVolmax=0
    for item in sortIndexList[-numOfmoodDay:]:
        tradeVolmax=tradeVolmax+curStock.dayTradeVolumeArray[-period:][item]
        print( curStock.dayStrList[-period:][item] )
    tradeVolmax=tradeVolmax/numOfmoodDay
    
    tradeVolmin=0
    print (u"交易量最小的交易日：")
    for item in sortIndexList[:numOfmoodDay]:
        tradeVolmin=tradeVolmax+curStock.dayTradeVolumeArray[-period:][item]
        print( curStock.dayStrList[-period:][item] )
    tradeVolmin=tradeVolmin/numOfmoodDay
    
    ##规定tradeVolmin+(tradeVolmax-tradeVolmin)*0.5 为 0.50
    ##计算情绪指数

    moodIndex50=tradeVolmin+(tradeVolmax-tradeVolmin)*0.5
    for i in range(100,0,-1):
        moodIndex=(curStock.dayTradeVolumeArray[-i]-moodIndex50)/moodIndex50+0.50
        print (u"{}情绪指数：{:.2f},次日涨幅{}".format(curStock.dayStrList[-i],moodIndex,curStock.dayRiseRateFList[-i+1]))


if __name__ == "__main__":
    print (u"市场情绪分析：")
    stockID='999999'
    print (u"市场整体情绪分析：")
    shStock=Stock(stockID)
    shStock.list2array()
    ## 应该考虑长期情绪指数和短期情绪指数
    moodIndex(shStock,100)
    moodIndex(shStock,15)
    ## 蓝筹市场、中小创市场判断,主要看 上证和深市的涨幅和人气对比
    print (u"市场类型判断")
    mymain()



