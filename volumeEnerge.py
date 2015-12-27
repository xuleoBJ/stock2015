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
from datetime import datetime,timedelta
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

##用periodCalDaysOfMood个交易日的交易量的 5个最大值的均值和5个最小值的均值的差的1/100作为基准值
def calMoodIndexBase(cStock,periodCalDaysOfMood=100):
    print ("-"*72)
    tradeVolumeArray=cStock.dayTradeVolumeArray[-periodCalDaysOfMood:]
#   计算最近periodCalDaysOfMood个交易日内的量能排序,通过量能分析市场情绪 
    sortIndexList=tradeVolumeArray.argsort()
    sortedArray=np.array(sorted(tradeVolumeArray))
 #   print sortIndexList 
    
    ##计算情绪指数选取的参数天数,由于有可能有极地量
    numOfmoodDay=5
    if periodCalDaysOfMood<20:
        numOfmoodDay=3

    print (u"{} {}个交易量最大的交易日：".format(cStock.stockID,numOfmoodDay))
    tradeVolMaxRef=sortedArray[-numOfmoodDay:].mean()
    for item in sortIndexList[-numOfmoodDay:]:
        print( cStock.dayStrList[-periodCalDaysOfMood:][item] )
    
    tradeVolMinRef=sortedArray[:numOfmoodDay].mean()
    print (u"{} {}个交易量最小的交易日：".format(cStock.stockID,numOfmoodDay))
    for item in sortIndexList[:numOfmoodDay]:
        print( cStock.dayStrList[-periodCalDaysOfMood:][item] )
    print ("-"*72)
    ##规定(tradeVolMaxRef-tradeVolMinRef)*0.01量作为基准情绪基数，
    moodIndexBase=(tradeVolMaxRef-tradeVolMinRef)*0.01
#    print tradeVolMaxRef,tradeVolMinRef,moodIndexBase
    return tradeVolMinRef,moodIndexBase


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

##period 是量能情绪控制周期，为选取的计算量能统计的时间范围,showDate
##由于创业板和股票发行日期的起始日期不同，只能选用 -1 倒数的指数方式
def moodIndexMarket(stockID="399001",showDateInterval=60,periodCalDaysOfMood=200):
    stockSH=Stock("999999")
    tradeVolBaseSH,moodIndexBaseSH =  calMoodIndexBase(stockSH,periodCalDaysOfMood)
    
    stockSZ=Stock("399001")
    tradeVolBaseSZ,moodIndexBaseSZ =  calMoodIndexBase(stockSZ,periodCalDaysOfMood)

    stockCYB=Stock("399006")
    tradeVolBaseCYB,moodIndexBaseCYB =  calMoodIndexBase(stockCYB,periodCalDaysOfMood)
    
    moodIndexSHList=[]
    moodIndexSZList=[]
    moodIndexCYBList=[]

    ##计算情绪指数 moodIndexSHList 长度是 periodCalDaysOfMood
    for i in range(-periodCalDaysOfMood,0):
        moodIndexSH=round( (stockSH.dayTradeVolumeArray[i]-tradeVolBaseSH)/moodIndexBaseSH , 2)
        moodIndexSHList.append(moodIndexSH)
        moodIndexSZ=round( (stockSZ.dayTradeVolumeArray[i]-tradeVolBaseSZ)/moodIndexBaseSZ , 2)
        moodIndexSZList.append(moodIndexSZ)
        moodIndexCYB=round( (stockCYB.dayTradeVolumeArray[i]-tradeVolBaseCYB)/moodIndexBaseCYB , 2)
        moodIndexCYBList.append(moodIndexCYB)
    
    print(u"-sh市场情绪趋势指数分析(基准=50)：")
    print(moodIndexSHList[-15:])
    print(u"-sz市场情绪趋势指数分析(基准=50)：")
    print(moodIndexSZList[-15:])
    print(u"-cyb市场情绪趋势指数分析(基准=50)：")
    print(moodIndexCYBList[-15:])
    
    
    mplDate=mpl.dates.date2num(stockSH.dateList[-showDateInterval:])
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays    = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%Y%m%d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    # Three subplots sharing both x/y axes
    fig, (ax, axStock) = plt.subplots(2, sharex=True, sharey=True)
    ax.plot(mplDate, moodIndexSHList[-showDateInterval:], '.--',label=u"shMI",color="b")
    ax.plot(mplDate, moodIndexSZList[-showDateInterval:], '.--',label=u"szMI",color="g")
    ax.plot(mplDate, moodIndexCYBList[-showDateInterval:], '.--',label=u"cybMI",color="c")
    ax.spines['left'].set_color('blue')
    ax.set_xlabel(u"日期")
    ax.set_ylabel(u"情绪指数")
    
   
    right_ax = ax.twinx() 
    right_ax.plot(mplDate, stockSH.dayPriceClosedFList[-showDateInterval:], '.-',label=u"收盘价",color="red")
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
    plt.title(u"{}市场分析".format(stockSH.stockID),color='r')

    fig.subplots_adjust(hspace=0.1)
   
    curStock=stockSZ
    if  stockID!="999999":
        curStock=Stock(stockID)

    tradeVolBase,moodIndexBase = calMoodIndexBase(curStock,periodCalDaysOfMood)
    moodIndexList=[]
    ##计算情绪指数
    for i in range(-periodCalDaysOfMood,0):
        moodIndex=round( (curStock.dayTradeVolumeArray[i]-tradeVolBase)/moodIndexBase , 2)
        moodIndexList.append(moodIndex)
    
    axStock.plot(mplDate, moodIndexList[-showDateInterval:], '.--',label=curStock.stockID+u"MI",color="b")
    axStock.spines['left'].set_color('blue')
    axStock.set_xlabel(u"日期")
    axStock.set_ylabel(u"情绪指数") 
    right_axStock = axStock.twinx() 
    right_axStock.plot(mplDate, curStock.day5TradeVolumeArray[-showDateInterval:], '.-',label=u"V_MA5",color="m")
    right_axStock.plot(mplDate, curStock.day10TradeVolumeArray[-showDateInterval:], '.-',label=u"V_MA10",color="c")
    right_axStock.plot(mplDate, curStock.day20TradeVolumeArray[-showDateInterval:], '.-',label=u"V_MA20",color="g")
    right_axStock.plot(mplDate, curStock.day60TradeVolumeArray[-showDateInterval:], '.-',label=u"V_MA60",color="y")
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
    rightAX2.plot(mplDate, curStock.dayPriceClosedArray[-showDateInterval:], '.-',label=u"price",color="r")
    

    h1, l1 = axStock.get_legend_handles_labels()
    h2, l2 = right_axStock.get_legend_handles_labels()
    h3, l3 = rightAX2.get_legend_handles_labels()
    plt.legend(h1+h2+h3, l1+l2+l3, loc=2)
    plt.title(u"{}分析".format(curStock.stockID),color='r')
    plt.show()

if __name__ == "__main__":
    print (u"市场情绪分析：")
    moodIndexMarket("399001",showDateInterval=100)
    


