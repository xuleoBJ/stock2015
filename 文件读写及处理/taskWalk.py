import os
import shutil

top="D:\\Ӣ���⾮����-������2013.9.28\\Ӣ���⾮����\\"
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        src=os.path.join(root, name)
        dst=os.path.join("D:\\copyLog",name)
        if src.endswith(".txt") or src.endswith(".TXT"):
            print(os.path.join(root, name))
            shutil.copyfile(src, dst) 
##    for name in dirs:
##        print(os.path.join(root, name))




