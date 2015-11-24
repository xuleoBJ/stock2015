# -*- coding: utf-8 -*- 
import matplotlib as mpl
from pylab import *
import matplotlib.pyplot as plt
from datetime import datetime
import time
from matplotlib import collections, transforms
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import candlestick,\
     plot_day_summary, candlestick_ohlc,volume_overlay3
from Cstock import Stock

def drawCandleStick(curStock,dateFind):
    mpl.rcParams['font.sans-serif'] = ['SimHei'] 

    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays    = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%Y-%m-%d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12

    #starting from dates expressed as strings...
    #...you convert them in float numbers....
    indexDate=curStock.dayStrList.index(dateFind)
    Prices=[]
    for i in range(indexDate-10,indexDate+10):
        Date = date2num(datetime.strptime(curStock.dayStrList[i], "%Y/%m/%d"))
    #so redefining the Prices list of tuples... date open high lowest close
        openPrice=curStock.dayPriceOpenFList[i]
        highestPrice=curStock.dayPriceHighestFList[i]
        lowestPrice=curStock.dayPriceLowestFList[i]
        closePrice=curStock.dayPriceClosedFList[i]
        tradeVolume=curStock.dayTradeVolumeFList[i]
        Prices.append([Date,openPrice,highestPrice, lowestPrice, closePrice,tradeVolume])
    print Prices
    
    PricesArray=np.array(Prices)
    #and then following the official example. 
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    candlestick_ohlc(ax, PricesArray, width=0.5,colorup='r', colordown='g')

    ax.yaxis.grid(True)
    ## add notation
    Xmark=matplotlib.dates.date2num(datetime.strptime(curStock.dayStrList[indexDate], "%Y/%m/%d"))
    Ymark=curStock.dayPriceClosedFList[indexDate]*0.5+curStock.dayPriceOpenFList[indexDate]*0.5
    ax.annotate("$", (Xmark,Ymark), xytext=(-2, 0), textcoords='offset points' )

    ax.xaxis_date()
    ax.autoscale_view()


    axVol = ax.twinx()
##
    dates = PricesArray[:,0]
    dates = np.asarray(dates)
    volume = PricesArray[:,5]
    volume = np.asarray(volume)

    # make bar plots and color differently depending on up/down for the day
    pos = PricesArray[:,1]-PricesArray[:,4]<0
    neg = PricesArray[:,1]-PricesArray[:,4]>0
    axVol.bar(dates[pos],volume[pos],color='red',width=0.5,align='center')
    axVol.bar(dates[neg],volume[neg],color='green',width=0.5,align='center')
    axVol.set_position(matplotlib.transforms.Bbox([[0.125,0.05],[0.9,0.2]]))
# Plot the volume overlay
#    bc = volume_overlay3(axVol, Prices,colorup='r', colordown='g', width=4, alpha=1.0)
#    yticks = axVol.get_yticks()
#    ymax=max(curStock.dayTradeVolumeFList[indexDate-10:indexDate+10])*1.5
#    axVol.set_ylim([0,ymax])
#    axVol.yaxis.set_label_position("right")
#    axVol.add_collection(bc)
#    corners = (0, 0), (len(bars), max(volumes))
#    axVol.update_datalim(corners)

    
    plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.title(u"{} {} 20日K".format(curStock.stockID,dateFind),color='r')
    plt.show()

if __name__=="__main__":
    stockID='999999'
    curStock=Stock(stockID)
    dateStr="2010/04/08"
    drawCandleStick(curStock,dateStr)
