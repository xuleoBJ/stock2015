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
    
    ## 如果当天预测行情不好，绝对不加仓买，宁可不动 
    ## 做T应该根据开盘价，大盘与个股的走势关系联动。高抛低吸。注意保持仓位。但是大盘必须是震荡市，不能是单边市
    ## 单边市和震荡市的判断，需要结合大盘和个股作分析。
    ## 如何T飞了 或者仓位不够的话，可以尾盘2：45再买回来！宁可不赚钱，不能赔钱。
    ## 弱势别想着暴涨，卖了就涨飞了？那种可能性也不是那么大的。一年也不会发生几回。而且平摊了仓位风险。亏不了多少。

    print(arrayDayPriceLowest[-5:])
    print(arrayDayPriceLowest[-5:].mean())
    
    print ("严格的执行止损方案。")
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


