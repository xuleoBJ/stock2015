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
#    print shStock.stockID,shStock.stockName,shStock.dayStrList[-5:],shStock.dayRadioLinkOfTradeVolumeFList[-5:]
#    print curStock.stockID,curStock.stockName,curStock.dayStrList[-5:],curStock.dayRadioLinkOfTradeVolumeFList[-5:]


##period 是量能情绪控制周期
def moodIndex(curStock,period):
#   计算最近period个交易日内的量能排序,通过量能分析市场情绪 
    sortIndexList=curStock.dayTradeVolumeArray[-period:].argsort()
#    print sortIndexList ## 输出指数，注意是 [-period:]中的位置
    
    ##负情绪指数
    tradeVolmax5=0 
    print (u"交易量最大的交易日：")
    for item in sortIndexList[-5:]:
        tradeVolmax5=tradeVolmax5+curStock.dayTradeVolumeArray[-period:][item]
        print( curStock.dayStrList[-period:][item] )
    tradeVolmax5=tradeVolmax5/5
     
    ##正情绪指数
    tradeVolmin5=0 
    print (u"交易量最小的交易日：")
    for item in sortIndexList[:5]:
        tradeVolmin5=tradeVolmax5+curStock.dayTradeVolumeArray[-period:][item]
        print( curStock.dayStrList[-period:][item] )
    tradeVolmin5=tradeVolmin5/5
    
    ##规定tradeVolmin5+(tradeVolmax5-tradeVolmin5)*0.5 为 0.50
    ##计算情绪指数

    moodIndex50=tradeVolmin5+(tradeVolmax5-tradeVolmin5)*0.5
    for i in range(5,0,-1):
        moodIndex=(curStock.dayTradeVolumeArray[-i]-moodIndex50)/moodIndex50+0.50
        print (u"{}情绪指数：{:.2f}".format(curStock.dayStrList[-i],moodIndex))


if __name__ == "__main__":
    print (u"成交量反应了市场情绪。")
    shStock=Stock('999999')
    shStock.list2array()
    stockID='399001'
    curStock=Stock(stockID)
    curStock.list2array()
    moodIndex(shStock,200)
    moodIndex(curStock,100)
    mymain()



