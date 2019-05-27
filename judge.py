# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:批量URL_Fuzz检测工具        *
#*********************************************

import re
# list = ['211.138.123.205 port 80 is open', '211.138.123.216 port 80 is open']
# list2 = ['221_181_128_141_80','211_138_123_223_80']
def re_judge(list2):
    list3 = []
    for i in open('reResult.txt','r'):
        list3.append(i)
    s = re.search(str(list2),str(list3))
    if s:
        print ('不存在异常端口')
        return True
    else:
        print('存在异常端口')
        return False


re_judge(['221_181_128_205_80','211_138_123_216_80'])