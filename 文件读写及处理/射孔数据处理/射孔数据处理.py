# -*- coding: cp936 -*-
import os
from datetime import *

def getTodayStr_YearMonth():
    currentYear=date.today().timetuple().tm_year
    currentMonth=date.today().timetuple().tm_mon
    return(str(currentYear*100+currentMonth))

def timeGenerate(startDate_str,endDay_str=getTodayStr_YearMonth(),fileWrited_path='连续时间序列.txt'):
    endYear=int(endDay_str)/100
    endDate=int(endDay_str)%100
    startYear=int(startDate_str)/100
    startMonth=int(startDate_str)%100
    fileOpendWrited=open(fileWrited_path,'w')
    while startYear<endYear:
        while  startMonth<=12:
            print(startYear*100+startMonth)
            fileOpendWrited.write(str(startYear*100+startMonth)+'\n')
            startMonth=startMonth+1
        startYear=startYear+1
        startMonth=1
    while startYear==endYear  and startMonth<endDate:
        print(startYear*100+startMonth)
        fileOpendWrited.write(str(startYear*100+startMonth)+'\n')
        startMonth=startMonth+1
    fileOpendWrited.close()
    print(os.path.abspath(fileWrited_path))
    
if __name__=="__main__":

    filePath_perforation="射孔数据处理.txt"
    print ('deal with...'+filePath_perforation)
    filePath_Wried_Perforation="_perforation_xl.txt"

    fileWrited=open(filePath_Wried_Perforation,'w')

    wellName_list=[]
    perforationDay_list=[]
    topDepth_list=[]
    bottomDepth_list=[]
    line_list=[]
    
    lineIndex=0
    endDate="201102"
    for line in open(filePath_perforation,'r').readlines():
        lineIndex=lineIndex+1
        if line!="" and lineIndex>1:
            fileWrited.write(line)
            line_list.append(line)
            splitLine=line.split()
            wellName_list.append(splitLine[0])
            perforationDay_list.append(splitLine[1])
            startDate=int(splitLine[1])
                        
            endYear=int(endDate)/100
            endMonth=int(endDate)%100
            startYear=startDate/100
            startMonth=startDate%100

            while startYear<endYear:
                while  startMonth<=12:
##                    print(startYear*100+startMonth)
                    splitLine[1]=str(startYear*100+startMonth)
                    fileWrited.write('\t'.join(splitLine)+'\n')
                    startMonth=startMonth+1
                startYear=startYear+1
                startMonth=1
            while startYear==endYear  and startMonth<endMonth:
##                print(startYear*100+startMonth)
                splitLine[1]=str(startYear*100+startMonth)
                fileWrited.write('\t'.join(splitLine)+'\n')
                startMonth=startMonth+1
                
                
##            if float(splitLine[2])>float(splitLine[3]):
##                print('line ' +lineIndex+'has mistake.')
##            topDepth_list.append(splitLine[2])
##            bottomDepth_list.append(splitLine[3])

    fileWrited.close()
    
