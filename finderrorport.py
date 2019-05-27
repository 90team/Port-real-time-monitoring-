# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:批量URL_Fuzz检测工具        *
#*********************************************

#功能实现：字符串相减
def fderror(path,second):
    # First = first
    Second = second
    list3 = []
    for i in open('reResult.txt','r'):
        list3.append(i)
    First = str(list3)
    for i in First :
        if i in Second :
            First = First.replace(i,"")
    print (First)
    print('异常端口是：'+ First,file=open(path,'w+'))