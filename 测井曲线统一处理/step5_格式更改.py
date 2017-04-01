import os
import shutil
import datetime

i_INVALID_VALUE=-999
##从TXT格式测井曲线中提取所需要的系列。
def main():
    dirPathLogFileTxt="log_txt_por_perm_so"
    dirPathGoal='log_txt_split'
    if not os.path.exists(dirPathGoal):
        os.mkdir(dirPathGoal)

    fileJobDoneList = os.listdir(dirPathGoal)
    
    for fileItem in os.listdir(dirPathLogFileTxt):
        if fileItem in fileJobDoneList:
            continue
        print ('-'*10,'Current deal...'+fileItem)
        fileOpened=open(dirPathLogFileTxt+'\\'+fileItem,'r')
        fileWritedPore=open(dirPathGoal+'\\'+fileItem.replace(".txt","_por.txt"),'w')
        fileWritedPerm=open(dirPathGoal+'\\'+fileItem.replace(".txt","_perm.txt"),'w')
        fileWritedSo=open(dirPathGoal+'\\'+fileItem.replace(".txt","_so.txt"),'w')
        lineIndex=0
        indexListSelectedLog=[]
        for line in fileOpened.readlines():
            lineIndex+=1
            splitLine=line.upper().split()
            if lineIndex>1:
                if 40>=float(splitLine[1]) > 0:
                    fileWritedPore.write( splitLine[0]+"\t"+splitLine[1]+"\n")
                if float(splitLine[2]) > 0:
                    fileWritedPerm.write( splitLine[0]+"\t"+splitLine[2]+"\n")
                if float(splitLine[3]) > 0:
                    fileWritedSo.write( splitLine[0]+"\t"+splitLine[3]+"\n")
                
        fileOpened.close()
        fileWritedPore.close()
        fileWritedPerm.close()
        fileWritedSo.close()
        print(fileItem+"job done.")


if __name__=="__main__":
    starttime = datetime.datetime.now()

    main()
    endtime = datetime.datetime.now()
    print ("耗时"+str((endtime - starttime).seconds))
