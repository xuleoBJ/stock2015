# -*- coding: cp936 -*-
##��������ʱ�����У�����startDay_str����ʽ"200106",endDay_strĬ��Ϊ��ǰ����ʱ�䣬�ļ�����·��

from datetime import *
import os
def getTodayStr_YearMonth():
    currentYear=date.today().timetuple().tm_year
    currentMonth=date.today().timetuple().tm_mon
    return(str(currentYear*100+currentMonth))

def timeGenerate(startDay_str,endDay_str=getTodayStr_YearMonth(),fileWrited_path='����ʱ������.txt'):
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
    

