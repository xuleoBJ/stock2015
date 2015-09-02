# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc

reload(sys)
sys.setdefaultencoding('utf-8')

lineWrited=[]

##根据涨幅，第二天趋势分析
##fList是需要分析的数据list，比如涨幅，或者高开数据，flow是数据区间的下限值，fHigh是数据区间的上限值
def countTrendByRiseRate(curStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(curStock.riseRateFList)-1):
        if fLow<=curStock.riseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("满足条件个数：{},>0的个数{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

##根据第一天的走势，第二天趋势分析
##fList是需要分析的数据list，比如涨幅，或者高开数据，flow是数据区间的下限值，fHigh是数据区间的上限值
def countTrendByOpenCloseRate(curStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(curStock.openCloseRateFList)-1):
        if fLow<=curStock.riseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("满足条件个数：{},>0的个数{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

if __name__=="__main__":
    Ccomfunc.printInfor()
    
    startClock=time.clock() ##记录程序开始计算时间

    ##读取股票代码，存储在curStock里
    stockID="600270"
    curStock=Cstock.Stock(stockID)

    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

    ##设置分析周期
    iDaysPeriodUser=len(curStock.dateStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]
   
    ##增加时间点统计，可以有趋势的效果

    ##分析不同交易周期内，统计不同涨幅的个数频率
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"个交易日内统计：\n涨幅区间个数:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.riseRateFList[-days:]))
            if i==10:
                _line="涨停版\t"+str(_num)
            else :
                _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')
    
    ##分析不同交易周期内，统计最低值的个数频率
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"个交易日内统计：\n最低值区间个数:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),map(lambda x,y:100*(x-y)/y,curStock.priceLowestFList[-days:],curStock.priceClosedFList[-days-1:-1])))
            if i==10:
                _line="涨停版\t"+str(_num)
            else :
                _line=str(i)+"到"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')

    ##分析不同交易周期内,高开低走，第二天的涨跌
    for i in range(-10,11):
        print("当日走势{}%-{}%，次日涨幅分布：".format(i,i+1))
        countTrendByOpenCloseRate(curStock,curStock.riseRateFList,i-0.1,i+0.1)
    ##分析涨停版，第二天高开的频率


    print("根据头天的涨幅，对次日数据进行分析预测：")
    for i in range(-10,11):
        print("当日涨幅{}%-{}%,次日高开分布：".format(i,i+1))
        countTrendByRiseRate(curStock,curStock.openRateFList,i-0.1,i+0.1)
    for i in range(-10,11):
        print("当日涨幅{}%-{}%，次日涨幅分布：".format(i,i+1))
        countTrendByRiseRate(curStock,curStock.riseRateFList,i-0.1,i+0.1)
#    for i in range(-10,11):
#        headLine=str(len(fList))+"个前一日涨幅区间："+str(j)+"到"+str(j+1)+",次日开盘幅度区间：" if i!=10 else "前一日涨停板,次日开盘幅度区间："
#        headLine=headLine+str(i)+"到"+str(i+1)+"个数：" if i!=10 else headLine+"涨停板"
#        _num=len(filter(lambda x:i<=x<i+1,fList))
#        _line=headLine+"\t"+str(_num)
#        print _line
#        fileWrited.write(_line+'\n')
    ##计算周期内涨的频率并绘直方图
    ##统计分析 近期大盘开盘点位和最低点的差额,这个只能近期有效，长期无效
    ##最近10个交易日的浮动是对做t最好的参考资料。而不能凭感觉说 低了，或者高了！！！！
    ##计算周期内涨的频率并绘直方图
    ##计算周期内涨的频率并绘直方图
    ##分析高开低走，低开高走，高开高走，低开低走的个数
    ##计算每天振幅的幅度分布并绘图
    ##涨停或者跌停出现的个数
    ##高开的天数，低开的天数
    ##设置分析周期
    ##成交量变动分析
#    print ("正在分析成交量变动：")
#    for i in range(-20,-1):
#        print curStock.dateStrList[i],curStock.riseOfTradeVolumeFList[i],curStock.riseOfTurnOverFList[i]
#    for i in range(-iDaysPeriodUser,-1):
#        ##这里变更条件找历史图行，又一周的行情分析
#        if curStock.riseRateFList[i-2]<=-3 and curStock.riseRateFList[i]>=3 and curStock.priceClosedFList[i-2]>curStock.priceClosedFList[i-1]:
#            if curStock.waveRateFList[i]>=3: ##振幅
#               if curStock.tradeVolumeFList[i-2]>curStock.tradeVolumeFList[i-1]>curStock.tradeVolumeFList[i]: ## 成交量
#                print(curStock.dateStrList[i])
#                fileWrited.write(curStock.dateStrList[i]+'\n')
#                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


