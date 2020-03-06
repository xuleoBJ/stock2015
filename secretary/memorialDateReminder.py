## 纪念日提醒

import time
from datetime import datetime
from tkinter import messagebox
from datetime import timedelta

if __name__=="__main__":
    today = datetime.today()
    start_time = time.time()
    print( time.strftime("%H:%M:%S -") + "开始工作时间")
    intervalSecond = 60*15 ##15分钟休息一下
    while 1:     
        time.sleep(intervalSecond)
        printInfo = time.strftime("%H:%M:%S -") +" 休息眼睛"
        messagebox.showinfo("提示",printInfo)
        
        time.sleep(intervalSecond)
        printInfo = time.strftime("%H:%M:%S -") +"活动腿脚"
        messagebox.showinfo("提示",printInfo)
        
