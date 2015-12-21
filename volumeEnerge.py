# -*- coding: UTF-8 -*-
import datetime
import lxml.etree as etree
import lxml.html
import ConfigParser
import time,sched,os,urllib2,re,string
import Ccomfunc,trendAna
import ctypes
from Cstock import Stock
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
from matplotlib.ticker import Formatter
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, DayLocator, MONDAY,YearLocator , MonthLocator 
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False  ## 负号问题

class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind >= len(self.dates) or ind < 0:
            return ''

        return self.dates[ind].strftime(self.fmt)

def calMoodIndexBase(cStock,matchDateIndex,periodCalDaysOfMood=200):
    print ("-"*72)
#   计算最近periodCalDaysOfMood个交易日内的量能排序,通过量能分析市场情绪 
    sortIndexList=cStock.dayTradeVolumeArray[matchDateIndex-periodCalDaysOfMood:matchDateIndex].argsort()
#    print sortIndexList ## 输出指数，注意是 [-periodCalDaysOfMood:]中的位置
    
    ##正情绪指数选取的参数天数
    numOfmoodDay=5
    if periodCalDaysOfMood<20:
        numOfmoodDay=3

#    print (u"{}个交易量最大的交易日：".format(numOfmoodDay))
    tradeVolmax=0
    for item in sortIndexList[matchDateIndex-numOfmoodDay:]:
        tradeVolmax=tradeVolmax+cStock.dayTradeVolumeArray[matchDateIndex-periodCalDaysOfMood:matchDateIndex][item]
#        print( cStock.dayStrList[-periodCalDaysOfMood:][item] )
    tradeVolmax=tradeVolmax/numOfmoodDay
    
    tradeVolmin=0
#    print (u"{}个交易量最小的交易日：".format(numOfmoodDay))
    for item in sortIndexList[:numOfmoodDay]:
        tradeVolmin=tradeVolmax+cStock.dayTradeVolumeArray[matchDateIndex-periodCalDaysOfMood:matchDateIndex][item]
#        print( cStock.dayStrList[-periodCalDaysOfMood:][item] )
    tradeVolmin=tradeVolmin/numOfmoodDay
    print ("-"*72)

    ##规定(tradeVolmax-tradeVolmin)*0.01量作为基准情绪基数，
    moodIndexBase=(tradeVolmax-tradeVolmin)*0.01
    return tradeVolmin,moodIndexBase


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

##period 是量能情绪控制周期，为选取的计算量能统计的时间范围,showDate
def moodIndexMarket(stockID="999999",strDate="",showDateInterval=60,periodCalDaysOfMood=200):
    stockSH=Stock("999999")
    stockSH.list2array()
    matchDateIndex = Ccomfunc.getIndexByStrDate(stockSH,strDate)
    
    tradeVolBaseSH,moodIndexBaseSH =  calMoodIndexBase(stockSH,matchDateIndex,periodCalDaysOfMood)
    
    stockSZ=Stock("399001")
    stockSZ.list2array()
    tradeVolBaseSZ,moodIndexBaseSZ =  calMoodIndexBase(stockSZ,matchDateIndex,periodCalDaysOfMood)

    stockCYB=Stock("399006")
    stockCYB.list2array()
    tradeVolBaseCYB,moodIndexBaseCYB =  calMoodIndexBase(stockCYB,matchDateIndex,periodCalDaysOfMood)
    
    moodIndexSHList=[]
    moodIndexSZList=[]
    moodIndexCYBList=[]

    ##计算情绪指数
    for i in range(matchDateIndex-periodCalDaysOfMood,matchDateIndex):
        moodIndexSH=round( (stockSH.dayTradeVolumeArray[i]-tradeVolBaseSH)/moodIndexBaseSH , 2)
        moodIndexSHList.append(moodIndexSH)
        moodIndexSZ=round( (stockSH.dayTradeVolumeArray[i]-tradeVolBaseSZ)/moodIndexBaseSZ , 2)
        moodIndexSZList.append(moodIndexSZ)
        moodIndexCYB=round( (stockCYB.dayTradeVolumeArray[i]-tradeVolBaseCYB)/moodIndexBaseCYB , 2)
        moodIndexCYBList.append(moodIndexCYB)
    
    print(u"-sh市场情绪趋势指数分析(基准=50)：")
    print(moodIndexSHList[matchDateIndex-15:matchDateIndex])
    print(u"-sz市场情绪趋势指数分析(基准=50)：")
    print(moodIndexSZList[matchDateIndex-15:matchDateIndex])
    print(u"-cyb市场情绪趋势指数分析(基准=50)：")
    print(moodIndexCYBList[matchDateIndex-15:matchDateIndex])
    
    
    mplDate=mpl.dates.date2num(stockSH.dateList[matchDateIndex-showDateInterval:matchDateIndex])
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays    = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%Y%m%d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    # Three subplots sharing both x/y axes
    fig, (ax, axStock) = plt.subplots(2, sharex=True, sharey=True)
    ax.plot(mplDate, moodIndexSHList[-showDateInterval:], '.--',label=u"sh情绪指数",color="y")
    ax.plot(mplDate, moodIndexSZList[-showDateInterval:], '.--',label=u"sz情绪指数",color="m")
    ax.plot(mplDate, moodIndexCYBList[-showDateInterval:], '.--',label=u"cyb情绪指数",color="c")
    ax.spines['left'].set_color('blue')
    ax.set_xlabel(u"日期")
    ax.set_ylabel(u"情绪指数")
    
   
    right_ax = ax.twinx() 
    right_ax.plot(mplDate, stockSH.dayPriceClosedFList[matchDateIndex-showDateInterval:matchDateIndex], '.-',label=u"收盘价",color="red")
    right_ax.spines['right'].set_color('red')
    #right_ax.set_ylim(-10,10)
    
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
#    formatter = MyFormatter(mplDate)
#    ax.xaxis.set_major_formatter(formatter)
    ax.autoscale_view()
    fig.autofmt_xdate()
   
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = right_ax.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, loc=2)
    plt.title(u"{}市场分析".format(stockSH.stockName),color='r')

    fig.subplots_adjust(hspace=0.1)
   
    cStock=stockSZ
    if  stockID!="999999":
        cStock=Stock(stockID)
        cStock.list2array()

    tradeVolBase,moodIndexBase =  calMoodIndexBase(cStock,matchDateIndex,periodCalDaysOfMood)
    moodIndexList=[]
    ##计算情绪指数
    for i in range(matchDateIndex-periodCalDaysOfMood,matchDateIndex):
        moodIndex=round( (cStock.dayTradeVolumeArray[i]-tradeVolBase)/moodIndexBase , 2)
        moodIndexList.append(moodIndex)
    
    axStock.plot(mplDate, moodIndexList[-showDateInterval:], '.-',label=u"MoodIndex",color="b")
    axStock.spines['left'].set_color('blue')
    axStock.set_xlabel(u"日期")
    axStock.set_ylabel(u"情绪指数") 
    right_axStock = axStock.twinx() 
    right_axStock.plot(mplDate, cStock.day5TradeVolumeArray[matchDateIndex-showDateInterval:matchDateIndex], '.--',label=u"VolumeMA5",color="m")
    right_axStock.plot(mplDate, cStock.day10TradeVolumeArray[matchDateIndex-showDateInterval:matchDateIndex], '.--',label=u"VolumeMA10",color="c")
    right_axStock.plot(mplDate, cStock.day20TradeVolumeArray[matchDateIndex-showDateInterval:matchDateIndex], '.--',label=u"VolumeMA20",color="g")
    right_axStock.plot(mplDate, cStock.day60TradeVolumeArray[matchDateIndex-showDateInterval:matchDateIndex], '.--',label=u"VolumeMA60",color="y")
   # right_axStock.spines['right'].set_color('red')

    rightAX2 = axStock.twinx()
    offset = 1.02
    rightAX2.spines["right"].set_position(("axes", offset))
    # Having been created by twinx, rightAX2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
    make_patch_spines_invisible(rightAX2)
    # Second, show the right spine.
    rightAX2.spines["right"].set_visible(True)
    rightAX2.spines['right'].set_color('r')
    rightAX2.plot(mplDate, cStock.dayPriceClosedArray[matchDateIndex-showDateInterval:matchDateIndex], '.-',label=u"price",color="r")
    

    h1, l1 = axStock.get_legend_handles_labels()
    h2, l2 = right_axStock.get_legend_handles_labels()
    h3, l3 = rightAX2.get_legend_handles_labels()
    plt.legend(h1+h2+h3, l1+l2+l3, loc=2)
    plt.title(u"{}分析".format(cStock.stockName),color='r')
    plt.show()

if __name__ == "__main__":
    print (u"市场情绪分析：")
    stockIDList=['999999',"399001"]
    moodIndexMarket(showDateInterval=200)
    
    print (u"市场整体情绪分析：")
#    for stockID in stockIDList:
#        cStock=Stock(stockID)
#        cStock.list2array()
#        ## 应该考虑长期情绪指数和短期情绪指数
#        moodIndex(cStock,200)
    ## 蓝筹市场、中小创市场判断,主要看 上证和深市的涨幅和人气对比



