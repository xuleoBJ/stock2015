#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@ 计算自然周第一天、自然月第一天和每天的凌晨时间戳
@ author : 
@ email  : 
@ mtime  : 
"""
import time
import datetime
 
def get_day_begin(ts = time.time(),N = 0):
    """
    N为0时获取时间戳ts当天的起始时间戳，N为负数时前数N天，N为正数是后数N天
    """
    return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d',time.localtime(ts)),'%Y-%m-%d'))) + 86400*N
 
def get_week_begin(ts = time.time(),N = 0):
    """
    N为0时获取时间戳ts当周的开始时间戳，N为负数时前数N周，N为整数是后数N周，此函数将周一作为周的第一天
    """
    w = int(time.strftime('%w',time.localtime(ts)))
    return get_day_begin(int(ts - (w-1)*86400)) + N*604800
 
def get_month_begin(ts = time.time(),N = 0):
    """
    N为0时获取时间戳ts当月的开始时间戳，N为负数前数N月，N为正数后数N月
    """
    month_day = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    cur_y,cur_m,cur_d = [int(x) for x in time.strftime('%Y-%m-%d',time.localtime(ts)).split('-')]
    if (cur_y%4 == 0 and cur_y%100 != 0) or cur_y%400 == 0:
        month_day[2] = 29
    else:
        month_day[2] = 28
    t = get_day_begin(ts) - (cur_d-1)*86400
    real_month = N + cur_m
    if real_month == cur_m:
        return t
    if N > 0:
        if real_month <= 12:
            for x in xrange(cur_m,real_month):
                t += month_day[x]*86400
        if real_month > 12:
            for x in xrange(cur_m,13):
                t += month_day[x]*86400
            t = get_month_begin(t,real_month - 13)
    if N < 0:
        if real_month >= 1:
            for x in xrange(real_month,cur_m):
                t -= month_day[x]*86400
        if real_month < 1:
            for x in xrange(1,cur_m):
                t -= month_day[x]*86400
            t -= month_day[12]*86400
            t = get_month_begin(t,real_month)
    return t
 
if __name__ == "__main__":
    #get current week num of the year
    dateStr="2016/07/10"
    dt = datetime.datetime.strptime(dateStr, "%Y/%m/%d")
    dtMon = dt + datetime.timedelta(days=( - dt.weekday()))
    print dtMon,dtMon.weekday()
    print dt
    now = datetime.date(2016, 7, 9)
    numWeek = now.isocalendar()[1]
    print ("本周是年度"+str(numWeek)+"星期"+str(now.weekday()))
    iWeekDay=0
    #The -0 and -%w pattern tells the parser to pick the sunday in that week. 
    for iYear in range(2010,2017):
        dtStr = "-".join([str(iYear),str(numWeek),str(iWeekDay)])
        dt = datetime.datetime.strptime(dtStr, "%Y-%W-%w")
        print(dt.strftime("%Y/%m/%d"))
        ##星期天为第0天
        print("本周的第"+dt.strftime("%w")+"天")
        print(u"星期"+str(dt.weekday()))
