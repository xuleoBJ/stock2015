## 到点时刻休息
import time
from datetime import datetime
from tkinter import messagebox
from datetime import timedelta

if __name__=="__main__":
    today = datetime.today()
    start_time = time.time()
    print( time.strftime("%H:%M:%S -") + "开始工作时间，请到点休息，起来活动活动。")
    lastRecordTime = start_time
    intervalSecond = 30
    while 1:
        restTime100= datetime(today.year, today.month,today.day,10,00,0)
        if  restTime100 <= datetime.now() < restTime100+timedelta(minutes=30):
            printInfo = time.strftime("%H:%M:%S -") + "中间休息"
            messagebox.showinfo("提示",printInfo)

        restTime300= datetime(today.year, today.month,today.day,15,0,0)
        if  restTime300 <= datetime.now() < restTime300+timedelta(minutes=30):
            printInfo = time.strftime("%H:%M:%S -") + "中间休息"
            messagebox.showinfo("提示",printInfo)

        time.sleep(intervalSecond)
        
