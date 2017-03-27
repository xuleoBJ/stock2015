import os
import shutil

top="D:\\英东测井数据-房国庆2013.9.28\\英东测井数据\\"
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        src=os.path.join(root, name)
        dst=os.path.join("D:\\copyLog",name)
        if src.endswith(".txt") or src.endswith(".TXT"):
            print(os.path.join(root, name))
            shutil.copyfile(src, dst) 
##    for name in dirs:
##        print(os.path.join(root, name))




