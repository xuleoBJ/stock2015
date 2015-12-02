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
