# -*- coding:utf-8 -*- 
## 提醒休息

import time
from datetime import datetime
from tkinter import messagebox
from datetime import timedelta

if __name__ == "__main__":
    _today = datetime.today()
    _start_time = time.time()
    print( "开始工作时间: " + time.strftime("%H:%M:%S") )
    iMin = 15
    intervalSecond = 60*iMin
    while 1:     
        time.sleep(intervalSecond)
        print( "当前时间: " + time.strftime("%H:%M:%S") )
        printInfo = time.strftime("%H:%M:%S -") +"您已经连续盯电脑" +str(iMin)+"分钟,请休息眼睛。"
        messagebox.showinfo("提示",printInfo)
        
        time.sleep(intervalSecond)
        print( "当前时间: " + time.strftime("%H:%M:%S") )
        printInfo = time.strftime("%H:%M:%S -") +"您已经连续盯电脑" +str(iMin)+"分钟,请活动拉升。"
        messagebox.showinfo("提示",printInfo)
        
