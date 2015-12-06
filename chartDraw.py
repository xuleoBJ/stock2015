# -*- coding: UTF-8 -*-
from __future__ import print_function
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import datetime
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY,YearLocator, MonthLocator
from Cstock import Stock

def format_date(x, pos=None):
    thisind = np.clip(int(x + 0.5), 0, N - 1)
    return r.date[thisind].strftime('%Y-%m-%d')

def barDraw():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, color='r', yerr=menStd)

    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(ind + width/2., ('hello', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks(np.arange(0, 81, 10))

    plt.show()

if __name__ == "__main__":
    shStock=Stock('999999')
    shStock.list2array()
    
    mplDate=mpl.dates.date2num(shStock.dateList)
    mplData=shStock.dayPriceClosedArray
# first we'll do it the default way, with gaps on weekends
    years = YearLocator()   # every year
    months = MonthLocator()  # every month
    yearsFmt = DateFormatter('%Y')
    fig, ax = plt.subplots()
    ax.plot(mplDate, mplData, 'o-')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    ax.autoscale_view()
    fig.autofmt_xdate()


    plt.show()
    barDraw()
