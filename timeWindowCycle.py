# -*- coding: UTF-8 -*-
import datetime
import ConfigParser
import time,sched,os,urllib2,re,string

def May(vDay):
    if vDay.month==5:
        print(u"5月整体提示,华尔街名言5月清仓，10月回来。")


def Weekends(vDay):
    if vDay.isoweekday()==5:
        print(u"周5及节假日效应必须考虑。当心黑色周一，特别是利空出尽的情况。")

if __name__ == "__main__":
    today=datetime.date.today()
    May(today)
    Weekends(today)
    



