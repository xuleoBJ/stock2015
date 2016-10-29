# -*- coding: UTF-8 -*-
import datetime
import ConfigParser
import time,sched,os,urllib2,re,string
import Ccomfunc

def May(vDay):
    if vDay.month==5:
        print(u"5月整体提示,华尔街名言5月清仓，10月回来。")


def Weekends(vDay):
    if vDay.isoweekday()==5:
        print(u"周5及节假日效应必须考虑。当心黑色周一，特别是利空出尽的情况。")

##判断所属周期的牛熊，读取文件，根据日期判断所属周期，如果涨幅-5 +5直接稳定状态，大于5 牛市，小于5熊市
##input 是 strDate
##读取周期文件
def getCycleType(curdate,timeWindowDataFile):
    dateList=[]
    riseRateList =[]
    if os.path.exists(timeWindowDataFile):
        fileOpened=open(timeWindowDataFile,'r')
        ##从文件中读取日数据，并计算构造相关的日数据
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex=lineIndex+1
            splitLine=line.split()
            if line!="" and lineIndex>3 and len(splitLine)>=5:
                tempDate = Ccomfunc.convertDateStr2Date(splitLine[0])
                dateList.append(tempDate)
                riseRateList.append( float(splitLine[4]) )
    print dateList
    print riseRateList
    for i in range(0,len(dateList)-1):
        if dateList[i]<= curdate <= dateList[i+1]:
            riseRate = riseRateList[i]
            if riseRate > 5:
                return 1
            elif -5<= riseRate <= 5 :
                return 0
            else :
                return -1

if __name__ == "__main__":
    today=datetime.date.today()
    filePath ="999999_250_peakAnalysisPrice.txt"
    strDate = "2015/10/10"
    curdate =  Ccomfunc.convertDateStr2Date(strDate)
    print getCycleType(curdate,filePath)
    May(today)
    Weekends(today)
    



