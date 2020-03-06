# -*- coding: cp936 -*-
import os

if __name__=="__main__":

##    print("当前工作路径：",os.getcwd())


    wellName=os.path.basename(os.getcwd())
    print ('按小层对解释成果表加权平均，读入文件是两个，\n”井号 小层名“，“井号 小层名 顶深 底深 孔渗饱”...')
    fileName_WellNameAndWelltop="wellName_layer.txt"
    fileName_JSCGB="jscgb.txt"
    
    openFileWrite="小层内加权分析结果.txt"


    fileOpened_WellNameAndWelltop=open(fileName_WellNameAndWelltop,'r')
    fileOpened_JSCGB=open(fileName_JSCGB,'r')
    
    fileWrited=open(openFileWrite,'w')


    jh_list=[]
    xcm_list=[]
    top_flist=[]
    bottom_flist=[]
    sh_flist=[]
    yxhd_flist=[]
    kxd_flist=[]
    stl_flist=[]
    bhd_flist=[]
    
    lineIndex=0
    for lineJSCGB in fileOpened_JSCGB.readlines():
        lineIndex=lineIndex+1
        if lineJSCGB!="" and lineIndex>1:
            splitline=lineJSCGB.split()
            jh_list.append(splitline[0])
            xcm_list.append(splitline[1])
            top_flist.append(float(splitline[2]))
            bottom_flist.append(float(splitline[3]))
            sh_flist.append(float(splitline[4]))
            yxhd_flist.append(float(splitline[5]))
            kxd_flist.append(float(splitline[6]))
            stl_flist.append(float(splitline[7]))
            bhd_flist.append(float(splitline[8]))

    welllName_list=[]
    layerSeriers_list=[]
    for lineZone in fileOpened_WellNameAndWelltop.readlines():
        if lineZone!="":
            splitline=lineZone.split()
            welllName_list.append(splitline[0])
            layerSeriers_list.append(splitline[1])
   
##    print(welllName_list,layerSeriers_list)
    for i in range(len(welllName_list)):
        top_currentList=[]
        bottom=-999.0
        sh_currentList=[]
        yxhd_currentList=[]
        kxd_currentList=[]
        stl_currentList=[]
        bhd_currentList=[]
        
        for j in range(len(jh_list)):
            if welllName_list[i]==jh_list[j] and layerSeriers_list[i]==xcm_list[j]:
                if top_flist>0:
                   top_currentList.append(top_flist[j])
                   sh_currentList.append(sh_flist[j])
                   yxhd_currentList.append(yxhd_flist[j])
                   kxd_currentList.append(kxd_flist[j])
                   stl_currentList.append(stl_flist[j])
                   bhd_currentList.append(bhd_flist[j])

        if len(top_currentList)>0:
            sh=0
            kxd=0
            kxd_weightHD=0
            stl=0
            stl_weightHD=0
            bhd=0
            bhd_weightHD=0
            sh=sum(sh_currentList)
            for k in range(len(sh_currentList)):
                if kxd_currentList[k]>0:
                    kxd_weightHD=kxd_weightHD+sh_currentList[k]
                    kxd=kxd+sh_currentList[k]*kxd_currentList[k]
                    
                if bhd_currentList[k]>0:
                    bhd_weightHD=bhd_weightHD+sh_currentList[k]
                    bhd=bhd+sh_currentList[k]*bhd_currentList[k]

                if stl_currentList[k]>0:
                    stl_weightHD=stl_weightHD+sh_currentList[k]
                    stl=stl+sh_currentList[k]*stl_currentList[k]


            if kxd_weightHD>0:
                kxd=round(kxd/kxd_weightHD,3)
            else:
                kxd=-999
            if bhd_weightHD>0:
                bhd=round(bhd/bhd_weightHD,3)
            else:
                bxd=-999

            if stl_weightHD>0:
               stl=round(stl/stl_weightHD,3)
            else:
                stl=-999
            line=welllName_list[i]+'\t'+layerSeriers_list[i]+'\t'+str(min(top_currentList))+'\t'+str(bottom)+'\t'+str(sh)+'\t'+str(sum(yxhd_currentList))+'\t'+str(kxd)+'\t'+str(stl)+'\t'+str(bhd)+'\t'+'\n'
            fileWrited.write(line)
        else:
            line=welllName_list[i]+'\t'+layerSeriers_list[i]+'\t-999'*7+'\n'
            fileWrited.write(line)
            
    fileWrited.close()
    
