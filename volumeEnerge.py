# -*- coding: UTF-8 -*-
import datetime
import lxml.etree as etree
import lxml.html
import ConfigParser
import time,sched,os,urllib2,re,string
import ctypes
from Cstock import Stock
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, DayLocator, MONDAY,YearLocator , MonthLocator 
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False  ## 负号问题

def calMoodIndexBase(cStock,period=200):
    print (u"{}日情绪指数分析".format(period))
    print ("-"*72)
#   计算最近period个交易日内的量能排序,通过量能分析市场情绪 
    sortIndexList=cStock.dayTradeVolumeArray[-period:].argsort()
#    print sortIndexList ## 输出指数，注意是 [-period:]中的位置
    
    ##正情绪指数选取的参数天数
    numOfmoodDay=5
    if period<20:
        numOfmoodDay=3
    
    print (u"{}个交易量最大的交易日：".format(numOfmoodDay))
    tradeVolmax=0
    for item in sortIndexList[-numOfmoodDay:]:
        tradeVolmax=tradeVolmax+cStock.dayTradeVolumeArray[-period:][item]
        print( cStock.dayStrList[-period:][item] )
    tradeVolmax=tradeVolmax/numOfmoodDay
    
    tradeVolmin=0
    print (u"{}个交易量最小的交易日：".format(numOfmoodDay))
    for item in sortIndexList[:numOfmoodDay]:
        tradeVolmin=tradeVolmax+cStock.dayTradeVolumeArray[-period:][item]
        print( cStock.dayStrList[-period:][item] )
    tradeVolmin=tradeVolmin/numOfmoodDay
    print ("-"*72)

    ##规定(tradeVolmax-tradeVolmin)*0.01量作为基准情绪基数，
    moodIndexBase=(tradeVolmax-tradeVolmin)*0.01
    return tradeVolmin,moodIndexBase

##period 是量能情绪控制周期，为选取的计算量能统计的时间范围
def moodIndex(stockID,period=200):
    cStock=Stock(stockID)
    cStock.list2array()
    tradeVolBase,moodIndexBase =  calMoodIndexBase(cStock,period)
    moodIndexList=[]
    ##计算情绪指数
    for i in range(period,0,-1):
        moodIndex=(cStock.dayTradeVolumeArray[-i]-tradeVolBase)/moodIndexBase
        moodIndexList.append(moodIndex)
   #     print (u"{}情绪指数：{:.2f}\t次日涨幅:{}".format(cStock.dayStrList[-i],moodIndex,cStock.dayRiseRateFList[-i+1]))
    
    mplDate=mpl.dates.date2num(cStock.dateList[-period:])
    mplData=moodIndexList
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays    = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%Y%m%d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    fig, ax = plt.subplots()
    ax.plot(mplDate, mplData, '.-',label=u"情绪指数",color="blue")
    ax.spines['left'].set_color('blue')
    ax.set_xlabel(u"日期")
    ax.set_ylabel(u"情绪指数")
    
#    ax.set_ylim(-20,100)
    
    right_ax = ax.twinx() 
    right_ax.plot(mplDate, cStock.dayPriceClosedFList[-period:], '.-',label=u"收盘价",color="red")
    right_ax.spines['right'].set_color('red')
    #right_ax.set_ylim(-10,10)

    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.autoscale_view()
    fig.autofmt_xdate()

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = right_ax.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2)
   # plt.legend(loc=0,prop={'size':8}) 
    plt.title(u"{}情绪指数分析".format(cStock.stockID),color='r')
    plt.show()

if __name__ == "__main__":
    print (u"市场情绪分析：")
    stockIDList=['999999',"399001"]
    print (u"市场整体情绪分析：")
    for stockID in stockIDList:
        ## 应该考虑长期情绪指数和短期情绪指数
        moodIndex(stockID,200)
    ## 蓝筹市场、中小创市场判断,主要看 上证和深市的涨幅和人气对比



