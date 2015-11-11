# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock

if __name__=="__main__":
    
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    curStock=Cstock.Stock('002001')
    
    print ("做T价格计算，做t是宁可错过，不能做错的方案。")
    arrayDayPriceLowest=np.array(curStock.dayPriceLowestFList)

    print(arrayDayPriceLowest[-5:])
    print(arrayDayPriceLowest[-5:].mean())
    
    print ("严格的执行止损方案。")
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


