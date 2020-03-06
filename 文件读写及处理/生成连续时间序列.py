# -*- coding: cp936 -*-
##生成连续时间序列，输入startDay_str，格式"200106",endDay_str默认为当前今天时间，文件保存路径

from datetime import *
import os
def getTodayStr_YearMonth():
    currentYear=date.today().timetuple().tm_year
    currentMonth=date.today().timetuple().tm_mon
    return(str(currentYear*100+currentMonth))

def timeGenerate(startDay_str,endDay_str=getTodayStr_YearMonth(),fileWrited_path='连续时间序列.txt'):
    endYear=int(endDay_str)/100
    endMonth=int(endDay_str)%100
    year_var=int(startDay_str)/100
    month_var=int(startDay_str)%100
    fileOpendWrited=open(fileWrited_path,'w')
    while year_var<endYear:
        while  month_var<=12:
            print(year_var*100+month_var)
            fileOpendWrited.write(str(year_var*100+month_var)+'\n')
            month_var=month_var+1
        year_var=year_var+1
        month_var=1
    while year_var==endYear  and month_var<endMonth:
        print(year_var*100+month_var)
        fileOpendWrited.write(str(year_var*100+month_var)+'\n')
        month_var=month_var+1
    fileOpendWrited.close()
    print(os.path.abspath(fileWrited_path))



if __name__ == "__main__":

    print(getTodayStr_YearMonth())
    timeGenerate("200003")
    

