# -*- coding: utf-8 -*- 
import matplotlib as mpl
from pylab import *
import matplotlib.pyplot as plt
from datetime import datetime
import time
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import candlestick,\
     plot_day_summary, candlestick_ohlc
from Cstock import Stock

mpl.rcParams['font.sans-serif'] = ['SimHei'] 
stockID='999999'
curStock=Stock(stockID)

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays    = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%Y-%m-%d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#starting from dates expressed as strings...
#...you convert them in float numbers....
dateFind="2003/05/28"
indexDate=curStock.dayStrList.index(dateFind)
Prices=[]
for i in range(indexDate-10,indexDate+10):
    Date = date2num(datetime.strptime(curStock.dayStrList[i], "%Y/%m/%d"))
#so redefining the Prices list of tuples... date open high lowest close
    openPrice=curStock.dayPriceOpenFList[i]
    highestPrice=curStock.dayPriceHighestFList[i]
    lowestPrice=curStock.dayPriceLowestFList[i]
    closePrice=curStock.dayPriceClosedFList[i]
    Prices.append((Date,openPrice,highestPrice, lowestPrice, closePrice))
print Prices

#and then following the official example. 
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick_ohlc(ax, Prices, width=0.5,colorup='r', colordown='g')

ax.yaxis.grid(True)
## add notation
Xmark=matplotlib.dates.date2num(datetime.strptime(curStock.dayStrList[indexDate], "%Y/%m/%d"))
Ymark=curStock.dayPriceClosedFList[indexDate]*0.5+curStock.dayPriceOpenFList[indexDate]*0.5
ax.annotate("$", (Xmark,Ymark), xytext=(-2, 0), textcoords='offset points' )

ax.xaxis_date()
ax.autoscale_view()
plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.title(u"{} {} 20日K".format(stockID,dateFind),color='r')
plt.show()
