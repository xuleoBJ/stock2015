# -*- coding: UTF-8 -*-
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import datetime
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY

def format_date(x, pos=None):
    thisind = np.clip(int(x + 0.5), 0, N - 1)
    return r.date[thisind].strftime('%Y-%m-%d')

if __name__ == "__main__":
    datafile = u'so_data.csv'
    r = mlab.csv2rec(datafile, delimiter=';')

# the dates in my example file-set are very sparse (and annoying) change the dates to be sequential
    for i in range(len(r)-1):
        r['date'][i+1] = r['date'][i] + datetime.timedelta(days=1)

# first we'll do it the default way, with gaps on weekends
    fig, ax = plt.subplots()
    ax.plot(r['date'], r['close'], 'o-')
    fig.autofmt_xdate()

# next we'll write a custom formatter
    N = 20
    ind = np.arange(N)  # the evenly spaced plot indices
    fig, ax = plt.subplots()
    ax.plot(r['date'], r['close'], 'o-')
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    fig.autofmt_xdate()

    plt.show()
