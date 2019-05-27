# -*- coding:UTF-8 -*-
"""
获取最新的文件名的名称
import os
file_dict = {}

lists = os.listdir('.')  # 先获取文件夹内的所有文件
for i in lists:  # 遍历所有文件
    if os.path.splitext(i)[1] == '.txt':
        print (i)
        ctime = os.stat(os.path.join('.', i)).st_ctime
        file_dict[ctime] = i  # 添加创建时间和文件名到字典
    else:
        print('×')
max_ctime = max(file_dict.keys())  # 取值最大的时间
print (file_dict[max_ctime])
"""
# import os
# file_dict = {}
# lists = os.listdir('.')  # 先获取文件夹内的所有文件
# for i in lists:  # 遍历所有文件
#     if os.path.splitext(i)[1] == '.txt':
#         print(i)
#         ctime = os.stat(os.path.join('.', i)).st_ctime
#         file_dict[ctime] = i  # 添加创建时间和文件名到字典
#         max_ctime = max(file_dict.keys())  # 取值最大的时间
#         newfile_name = file_dict[max_ctime]  # 最新文件名
#         print ('-------------')
#         print (newfile_name)
# import time
# def mkdir(path):
#     # 引入模块
#     import os
#     # 去除首位空格
#     path = path.strip()
#     # 去除尾部 \ 符号
#     path = path.rstrip("\\")
#     # 判断路径是否存在
#     # 存在     True
#     # 不存在   False
#     isExists = os.path.exists(path)
#     # 判断结果
#     if not isExists:
#         # 如果不存在则创建目录
#         # 创建目录操作函数
#         os.makedirs(path)
#         print (path + ' 创建成功')
#         return True
#     else:
#         # 如果目录存在则不创建，并提示目录已存在
#         print (path + ' 目录已存在')
#         return False
#
#
# # 定义要创建的目录
# nowtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
# mkpath = nowtime
# # 调用函数
# mkdir(mkpath)
# 定义要创建的目录
# import time
# import dir_creater
#
# dir_nowtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
# mkpath = dir_nowtime
# dir_creater.mkdir(mkpath)
#
# for ip in open('hosts.txt', 'r'):
#     port = '80'
#     nowtime = time.strftime("%Y-%m-%d")
#     text_path = dir_nowtime + '/' + ip.replace('.', '_').strip() + '-' + nowtime + '.txt'
#     with open(text_path, 'w') as f:
#         f.writelines('{0} port {1} is open'.format(ip.strip(), port))
#         f.writelines('\n')
#
# list = []
# list_str = str(list)
# print (len(list_str))
#判断是否存在异常端口
# import re
# list = ['211.138.123.205 port 80 is open', '211.138.123.216 port 80 is open']
# list2 = ['221_181_128_141_80','211_138_123_223_80']
# list3 = ['']
# for i in open('reResult.txt','r'):
#     list3.append(i)
# s = re.search(str(list2),str(list3))
# if s:
#     print ('不存在异常端口')
# else:
#     print('存在异常端口')
print (open('hosts.txt','r').read())